from django.shortcuts import render, redirect
from .models import Location
from .models import Paiement
from users.models import Profile
from django.db.models import Q
from datetime import date
from voiture.models import Voiture  

import pdfkit
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.http import JsonResponse

import os
from django.conf import settings
from django.http import HttpResponse
#from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.
def mode_paiement(request):
    today = date.today()
    if 'q' in request.GET:
        q = request.GET['q']
        loca = Location.objects.filter(Q(nom_Client__nom__icontains=q)).filter(dt_demande__year=today.year, dt_demande__month=today.month, dt_demande__day=today.day)
    else:
        loca = Location.objects.filter(dt_demande__year=today.year, dt_demande__month=today.month, dt_demande__day=today.day)
    context = {'loc_pay': loca}
    return render(request, 'paiement/acceuil_paiement.html', context)

def ajout_paiement(request, pk):
    location = Location.objects.get(id=pk)
    clientLoueur = Profile.objects.exclude(user__isnull=True)
    if request.method == "GET":
        return render(request, 'paiement/paiement.html', {'locations': location, 'client_Loueur': clientLoueur})
    elif request.method == "POST":
       montants = request.POST.get("total")
       num_compte = request.POST.get("num_compte")
       date_pay = request.POST.get("date_pay")
       id_loc = request.POST.get("id_loc")
       loc = Location.objects.get(id=id_loc)
       loueur = request.POST.get("loueurUser")
       userloueur = Profile.objects.get(id=loueur)
       donne = Paiement(total=montants, num_compte=num_compte, date_pay=date_pay, id_loc=loc, loueurUser=userloueur)
       donne.save()
       return redirect('final_page')
    else:
       return render(request, 'paiement/paiement.html', {
        'loc': Location.objects.all()
       })

def final_page(request):
    pay = Paiement.objects.all().order_by('-id')[:1]
    if 'q' in request.GET:
        q = request.GET['q']
        paiement = Paiement.objects.filter(Q(id_loc__nom_Client__icontains=q))
    else:
        paiement = Paiement.objects.all()    
        context = {'pay': pay, 'paiement': paiement}
        return render(request, 'final_page/page_final.html', context)

def generer(request, id):
    paiement = Paiement.objects.get(id=id)
    template_path = 'final_page/generer.html'
    context = {'paiement': paiement}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Reçu_paiement.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response )
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def preparation_pay(request):
    nom_client = Location.objects.all()
    num_loc = Location.objects.all()
    nom_louer = Profile.objects.exclude(user__isnull=True)
    num_Vehi = Voiture.objects.all().exclude(condition="Accepter")
    montant_prix = Voiture.objects.all().exclude(condition="Accepter")
    if request.method == "POST":
        total = request.POST.get("total")
        date_pay = request.POST.get("date_pay")
        loueurUser = request.POST.get("loueurUser")
        lUser = Profile.objects.get(id=loueurUser)
        id_loc = request.POST.get("id_loc")
        loc_id = Location.objects.get(id=id_loc)
        donne = Paiement(total=total, date_pay=date_pay, loueurUser=lUser, id_loc=loc_id)
        donne.save()
        #return redirect("")
    context = {'nom_client': nom_client, 'num_loc': num_loc, 'nom_louer': nom_louer, 'num_Vehi': num_Vehi, 'montant_prix': montant_prix}
    return render(request, 'paiement/preparation_pay.html', context) 

def paiement_form(request):
    nom_client = Location.objects.all()
    num_loc = Location.objects.all()
    nom_louer = Profile.objects.exclude(user__isnull=True)
    num_Vehi = Voiture.objects.all().exclude(condition="Accepter")
    montant_prix = Voiture.objects.all().exclude(condition="Accepter")
    if request.method == "POST":
        total = request.POST.get("total")
        date_pay = request.POST.get("date_pay")
        num_compte = request.POST.get("num_compte")
        loueurUser = request.POST.get("loueurUser")
        lUser = Profile.objects.get(id=loueurUser)
        id_loc = request.POST.get("id_loc")
        loc_id = Location.objects.get(id=id_loc)
        donne = Paiement(total=total, date_pay=date_pay, loueurUser=lUser, id_loc=loc_id, num_compte=num_compte)
        donne.save()
        #return redirect("")
    context = {'nom_client': nom_client, 'num_loc': num_loc, 'nom_louer': nom_louer, 'num_Vehi': num_Vehi, 'montant_prix': montant_prix}
    return render(request, 'paiement/paiement_form.html', context)    



    
   