from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from location.models import Location
from users.models import Profile
from agence.models import Agence
from voiture.models import Voiture

from django.db.models import Q
from datetime import date

import pdfkit
from django.template.loader import get_template
from django.http.response import HttpResponse
from django.http import JsonResponse
import os
from django.conf import settings
from django.http import HttpResponse
#from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.
def acceuil_demande_location(request):
    if 'q' in request.GET:
        q = request.GET['q']
        agence = Agence.objects.filter(Q(nom_agence__icontains=q))
    else: 
        agence = Agence.objects.all()
    context = {'agen': agence}
    return render(request, 'location/acceuil_demande_location.html', context)

def envoie_demande(request, pk):
    today = date.today()
    client = Profile.objects.filter(user__isnull=True).filter(date_nais__year__lte=1999).filter(date_nais__year__gte=1987)
    loueur = Profile.objects.exclude(user__isnull=True)
    agenceInfo = Agence.objects.get(id=pk)
    if request.method == "GET":
        return render(request, 'location/demande_location.html', {'agenInfo': agenceInfo, 'clients': client, 'loueur': loueur})
    elif request.method == "POST":
        dt_demande = request.POST.get("dt_demande")
        type_loc = request.POST.get("type_loc")
        dure = request.POST.get("dure")
        destination = request.POST.get("destination")
        motif = request.POST.get("motif")
        dt_debut = request.POST.get("dt_debut")
        dt_fin = request.POST.get("dt_fin")
        autre_cond = request.POST.get("autre_cond")
        nom_autre = request.POST.get("nom_autre")
        email_autre = request.POST.get("email_autre")
        cin_autre = request.POST.get("cin_autre")
        permis_autre = request.POST.get("permis_autre")
        adresse_autre = request.POST.get("adresse_autre")
        loueur = request.POST.get("loueur")
        userloueur = Profile.objects.get(id=loueur)
        nom_agence = request.POST.get("nom_Agence")
        nomAgence = Agence.objects.get(id=nom_agence)
        nom_client = request.POST.get("nom_Client")
        nomClient = Profile.objects.get(id=nom_client)
        donnee = Location(dt_demande=dt_demande, type_loc=type_loc, dure=dure, destination=destination,
                          motif=motif, dt_debut=dt_debut, dt_fin=dt_fin, autre_cond=autre_cond, nom_autre=nom_autre,
                          email_autre=email_autre, nom_Client=nomClient, cin_autre=cin_autre, permis_autre=permis_autre,
                          adresse_autre=adresse_autre, nom_Agence=nomAgence, loueur=userloueur
                          )
        donnee.save()
        return redirect('acceuil')
    else:
    
        return render(request, 'location/demande_location.html') 

def procedure(request):
    today = date.today()
    client = Profile.objects.filter(user__isnull=True).filter(date_nais__year__lte=1999).filter(date_nais__year__gte=1987)
    agence = Agence.objects.all().exclude(userLoueur__isnull=True)
    agenceUser = Agence.objects.exclude(userLoueur__isnull=True)
    loueur = Profile.objects.exclude(user__isnull=True)
    loueurUser = Profile.objects.exclude(user__isnull=True)
    #vehicule = Vehicule.objects.all().exclude(condition="Accepter")
    if request.method == "POST":
        dt_demande = request.POST.get("dt_demande")
        type_loc = request.POST.get("type_loc")
        destination = request.POST.get("destination")
        autre_cond = request.POST.get("autre_cond")
        nom_autre = request.POST.get("nom_autre")
        email_autre = request.POST.get("email_autre")
        cin_autre = request.POST.get("cin_autre")
        permis_autre = request.POST.get("permis_autre")
        adresse_autre = request.POST.get("adresse_autre")
        nom_agence = request.POST.get("nom_Agence")
        nomAgence = Agence.objects.get(id=nom_agence)
        loueurs = request.POST.get("loueur")
        agenceLoueur = Profile.objects.get(id=loueurs)
        nom_client = request.POST.get("nom_Client")
        nomClient = Profile.objects.get(id=nom_client)
        donnee = Location(dt_demande=dt_demande, type_loc=type_loc, destination=destination,
                          autre_cond=autre_cond, nom_autre=nom_autre,
                          email_autre=email_autre, cin_autre=cin_autre, permis_autre=permis_autre,
                          adresse_autre=adresse_autre, nom_Client=nomClient, 
                          nom_Agence=nomAgence, loueur=agenceLoueur
                          )
        donnee.save()
        return redirect('pay_form')
    else:
        
        context = {'client': client, 'agence': agence, 'loueurAgence': loueur, 'agenceUser': agenceUser, 'loueurUser': loueurUser}
        return render(request, 'location/procedure.html', context)        

def imprimerAgence(request, id):
    agen = Agence.objects.get(id=id)
    template_path = 'location/impression.html'
    context = {'agen': agen}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Information_agence.pdf"'
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
   

# def nb_location(request):
#     if request.method == "POST":
#         if request.POST.get('num_loc'):
#             x = request.POST.get("num_loc")
#             z = request.POST.get("nom_Client")
#             loc = Client.objects.select_for_update().get(id_client=z)
#             loc.num_loc = x
#             loc.save()
#         return redirect('acceuil')
#     else:
#         return render(request, 'location/comfirm_loc.html', {
#             'client': Client.objects.all()
#         })


