from django.db.models import Count
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm
from django.core.mail import send_mail

from .models import Profile
from agence.models import Agence
from django.contrib.auth.models import User
from location.models import Location
from voiture.models import Voiture
from paiement.models import Paiement

from datetime import datetime
from datetime import date
from django.db.models import Sum, Max
from django.template import loader
from django.db.models import Q
import folium

def acceuil_inscription(request):
    return render(request, 'client/acceuil_inscription.html')

def home(request):
    return render(request, 'client/loueur/acceuil_loueur.html')

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'client/loueur/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
   
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'client/loueur/password_reset.html'
    email_template_name = 'client/loueur/password_reset_email.html'
    subject_template_name = 'client/loueur/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'client/loueur/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def home_loueur(request):
    today = date.today()
    try:
       userloueur = Profile.objects.get(user=request.user)    
       #locationList = list(Location.objects.filter(loueur=userloueur))
       locationList = Location.objects.all().filter(loueur=userloueur)
       locationList_navigation = Location.objects.all().filter(loueur=userloueur).filter(dt_demande__year=today.year, dt_demande__month=today.month, dt_demande__day=today.day)
       count_notifi = Location.objects.all().filter(loueur=userloueur).filter(dt_demande__year=today.year, dt_demande__month=today.month, dt_demande__day=today.day).count()
       reservation = list(Voiture.objects.filter(client_loueur=userloueur))
       #reservation = Vehicule.objects.all().filter(condition="Accepter").filter(client_loueur=userloueur)
       listPay = list(Paiement.objects.filter(loueurUser=userloueur))
       nbLocation = Location.objects.filter(loueur=userloueur).count()
       nbrReservation = Voiture.objects.filter(client_loueur=userloueur).count()
       totalPay = Paiement.objects.filter(loueurUser=userloueur).aggregate(Sum('total'))['total__sum']
       maxPay = Paiement.objects.filter(loueurUser=userloueur).aggregate(Max('total'))['total__max']
    except Location.DoesNotExist:
        return HttpResponseRedirect(reverse(""))
    
    if 'q' in request.GET:
        q = request.GET['q']
        reservation = Voiture.objects.filter(Q(id_location__id__icontains=q))
    elif 'search' in request.GET:
        search = request.GET['search']    
        listPay = Paiement.objects.filter(Q(id_loc__id__icontains=search))

    if request.method == 'POST':
       
        nom_agence = request.POST.get("nom_agence")
        adresse_agence = request.POST.get("adresse_agence")
        tel_agence = request.POST.get("tel_agence")
        email_agence = request.POST.get("email_agence")
        fax_agence = request.POST.get("fax_agence")
        profUser = Profile.objects.get(user=request.user)
       
        donne = Agence(nom_agence=nom_agence, adresse_agence=adresse_agence, tel_agence=tel_agence, email_agence=email_agence,
                       fax_agence=fax_agence, userLoueur=profUser)
        donne.save()
        
    context = {
        'nbLocation': nbLocation,
        'locationList': locationList,
        'reservation': reservation,
        'nbrReservation': nbrReservation,
        'listPay': listPay,
        'totalPay': totalPay,
        'maxPay': maxPay,
        'locationList_navigation': locationList_navigation,
        'count_notifi': count_notifi
        }
    return render(request, 'client/loueur/dashboard/home_loueur.html', context)

@login_required
def pay_reservation(request):
    userloueur = Profile.objects.get(user=request.user)
    x = list(Paiement.objects.filter(loueurUser=userloueur))
    meses = ['jan', 'fev', 'mar', 'avr', 'mai', 'juin', 'juil', 'aout', 'sept', 'octo', 'nov', 'dec']
    data = []
    labels = []
    cont = 0
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12):
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1

        y = sum([i.total for i in x if i.date_pay.month == mes and i.date_pay.year == ano])
        labels.append(meses[mes-1])
        data.append(y)
        cont += 1

    data_json = {'data': data[::-1], 'labels': labels[::-1]}
    return JsonResponse(data_json)

@login_required        
def demande_pay(request):
    userloueur = Profile.objects.get(user=request.user)
    dm_location = list(Location.objects.filter(loueur=userloueur))
    label = []
    data = []
 
    for location in dm_location:
        pai = Paiement.objects.filter(id_loc=location).aggregate(Sum('total'))
        if not pai['total__sum']:
            pai['total__sum'] = 0
        label.append(location.id)
        data.append(pai['total__sum'])

    x = list(zip(label, data))
    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))

    return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})

@login_required
def modification(request, pk=None):
    loc_modi = Location.objects.filter(id=pk).first()

    if request.method == "POST":
        loc_modi.type_loc = request.POST['type_loc']
        loc_modi.dt_demande = request.POST['dt_demande']
        #loc_modi.dure = request.POST['dure']
        loc_modi.destination = request.POST['destination']
        #loc_modi.motif = request.POST['motif']
        # loc_modi.dt_debut = request.POST['dt_debut']
        # loc_modi.dt_fin = request.POST['dt_fin']
        loc_modi.autre_cond = request.POST['autre_cond']
        loc_modi.nom_autre = request.POST['nom_autre']
        loc_modi.email_autre = request.POST['email_autre']
        loc_modi.cin_autre = request.POST['cin_autre']
        loc_modi.permis_autre = request.POST['permis_autre']
        loc_modi.adresse_autre = request.POST['adresse_autre']

        loc_modi.save()
        messages.success(request, 'un demande de location a été modifier avec success!')
        return redirect('home_loueur')
    context = {'loc_modi': loc_modi}
    template = loader.get_template('client/loueur/dashboard/modification_location.html')
    return HttpResponse(template.render(context, request))

# Modification reservation
@login_required
def modification_reservation(request, pk=None):
    reserv_modi = Voiture.objects.filter(id=pk).first()
    if request.method == "POST":
       reserv_modi.numImm = request.POST['numImm']
       reserv_modi.numSerie = request.POST['numSerie'] 
       reserv_modi.kilometrage = request.POST['kilometrage']
       reserv_modi.type_vehicule = request.POST['type_vehicule']
       reserv_modi.marque_vehicule = request.POST['marque_vehicule']
       reserv_modi.prixJ = request.POST['prixJ']
       
       reserv_modi.save()
       messages.success(request, 'un réservation a été modifier avec success!')
       return redirect('home_loueur')
    context = {'reserve': reserv_modi}
    template = loader.get_template('client/loueur/dashboard/modification_reservation.html')
    return HttpResponse(template.render(context, request))

# Detail du client
def detail_client(request, pk):
    #detailClient = Profile.objects.all()
    locations = Location.objects.get(id=pk)
    context = {'locs': locations}
    return render(request, 'client/loueur/dashboard/details_location.html', context)

#suppression demande de location
@login_required
def suppression(request, pk):
    loc = Location.objects.get(id=pk)
    if request.method == "POST":
        loc.delete()
        messages.error(request, 'Un demande de location a éte suprimer avec succes')
        return redirect("home_loueur")
    context = {'loc': loc}
    return render(request, 'client/loueur/dashboard/suppreListe.html', context)

#suppression reservation
@login_required
def suppression_reservation(request, pk):
    vehi = Voiture.objects.get(id=pk)
    if request.method == "POST":
        vehi.delete()
        messages.error(request, 'Un réservation a éte suprimer avec succes')
        return redirect("home_loueur")
    context = {'vehi': vehi}
    return render(request, 'client/loueur/dashboard/supprimeReservation.html', context)

#suppression de paiement
@login_required
def suppression_paiement(request, pk):
    pay = Paiement.objects.get(id=pk)
    if request.method == "POST":
        pay.delete()
        messages.error(request, 'Un paiement a éte suprimer avec succes')
        return redirect("home_loueur")
    context = {'pay': pay}
    return render(request, 'client/loueur/dashboard/supprimePaiement.html', context)

@login_required
def map_direction(request):
    return render(request, 'client/loueur/dashboard/map.html')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('home_loueur')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'client/loueur/dashboard/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def inscription(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        date_nais = request.POST.get("date_nais")
        email = request.POST.get("email")
        tel = request.POST.get("tel")
        ville = request.POST.get("ville")
        adresse = request.POST.get("adresse")
        cin = request.POST.get("cins")
        nation = request.POST.get("nation")
        cd_poste = request.POST.get("cd_poste")
        num_permis = request.POST.get("num_permis")
        sex = request.POST.get("sex")
        if len(request.FILES) != 0:
            photo = request.FILES["avatar"]
        donne = Profile(nom=nom, date_nais=date_nais, email=email, tel=tel, ville=ville,
                       adresse=adresse, cins=cin, nation=nation, cd_poste=cd_poste, num_permis=num_permis, sex=sex, avatar=photo)
        donne.save()
        messages.success(request, 'Votre inscription a bien envoyer!')
        return redirect('a_demande_loc')
    return render(request, 'client/inscription.html')


def contact(request):
   if request.method == "POST":
      name = request.POST.get("full-name")
      email = request.POST.get("email")
      subject = request.POST.get("subject")
      message = request.POST.get("message")
      data = {
         'name':name,
         'email':email,
         'subject':subject,
         'message':message
      }

      message = """
      New message: {}

      From: {}
        """.format(data['message'], data['email'])
      send_mail(data['subject'], message, '', ['selonrandriavao209@gmail.com'])
   return render(request, 'base/contact.html',{})    

# Page not found 404
def page_not_found(request):
    return render(request, 'base/page404.html')