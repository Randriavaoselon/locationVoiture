from django.shortcuts import render
from vehicule.models import Vehicule
from django.shortcuts import render, redirect
from users.models import Profile
from agence.models import Agence
#from .models import Vehicule
from location.models import Location
from users.models import Profile
from django.db.models import Q
from datetime import date

from django.contrib.auth.models import User

from django.contrib import messages

# Create your views here.

def acceuil_reservation(request):
    today = date.today()
    if 'q' in request.GET:
        q = request.GET['q']
        loca = Location.objects.filter(Q(nom_Client__nom__icontains=q)).filter(dt_demande__year=today.year, dt_demande__month=today.month, dt_demande__day=today.day)
    else:
        loca = Location.objects.filter(dt_demande__year=today.year, dt_demande__month=today.month, dt_demande__day=today.day)
    context = {'loc': loca}
    return render(request, 'vehicule/acceuil_reservation.html', context)

def ajout_vehicule(request):
    if request.method == "POST":
        numImm = request.POST.get("numImm")
        numSerie = request.POST.get("numSerie")
        dateMiseEnCirc = request.POST.get("dateMiseEnCirc")
        kilometrage = request.POST.get("kilometrage")
        type_vehicule = request.POST.get("type_vehicule")
        marque_vehicule = request.POST.get("marque_vehicule")
        prixJ = request.POST.get("prixJ")
        profUser = Profile.objects.get(user=request.user)
        #prixKm = request.POST.get("prixKm")
        condition = request.POST.get("condition")
        if len(request.FILES) != 0:
            photo = request.FILES["photos"]
        donne = Vehicule(numImm=numImm, dateMiseEnCirc=dateMiseEnCirc, kilometrage=kilometrage, type_vehicule=type_vehicule, 
                         marque_vehicule=marque_vehicule, condition=condition, photos=photo, numSerie=numSerie, 
                         prixJ=prixJ, client_loueur=profUser)    
        donne.save()
        messages.success(request, 'Un vehicule a été enregistrer avec succes')
        return redirect('home_loueur')
    return render(request, 'client/loueur/dashboard/ajout_vehicule.html')



def liste_vehicule(request):
    if 'q' in request.GET:
        q = request.GET['q']
        listeV = Vehicule.objects.filter(Q(marque_vehicule__icontains=q)|Q(type_vehicule__icontains=q)).filter(condition="Accepter")
    else:    
        listeV = Vehicule.objects.filter(condition="Accepter")
    context = {"liste": listeV}
    return render(request, "vehicule/liste_voiture.html", context)

# Detail vehicule
def detail_vehicule(request, pk):
    vehicule = Vehicule.objects.get(id=pk)
    context = {'vehi': vehicule}
    return render(request, 'vehicule/detail_vehicule.html', context)

#reserve vehicule
def reserve_vehicule(request, pk):
    vehicule = Vehicule.objects.get(id=pk)
    if request.method == "POST":
        #numImm = request.POST.get("numImm")
        type_vehicule = request.POST.get("type_vehicule")
        marque_vehicule = request.POST.get("marque_vehicule")
        date_reservetion = request.POST.get("date_reservetion")
        kilometrage = request.POST.get("kilometrage")
        type_prix = request.POST.get("type_prix")
        #prixKm = request.POST.get("prixKm")
        prixJ = request.POST.get("prixJ")
        dt_debut = request.POST.get("dt_debut")
        dt_fin = request.POST.get("dt_fin")
        jours = request.POST.get("jours")
        montant_total = request.POST.get("montant_total")
        #parite inscription
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
        # proprietaire = request.POST.get("client_loueur")
        # propri = Profile.objects.get(id=proprietaire)
        if len(request.FILES) != 0:
            photo = request.FILES["avatar"]

        donne1 = Vehicule(type_vehicule=type_vehicule,
                        marque_vehicule=marque_vehicule, type_prix=type_prix, date_reservetion=date_reservetion, 
                        prixJ=prixJ, dt_debut=dt_debut, dt_fin=dt_fin, jours=jours, montant_total=montant_total,
                        kilometrage=kilometrage)

        donne2 = Profile(nom=nom, date_nais=date_nais, email=email, tel=tel, ville=ville,
                       adresse=adresse, cins=cin, nation=nation, cd_poste=cd_poste, num_permis=num_permis, sex=sex, avatar=photo)
        donne2.save()
        donne1.save()
       
        return redirect('procedure') 
    context = {'vehicule': vehicule}
    return render(request, 'vehicule/reservation.html', context)