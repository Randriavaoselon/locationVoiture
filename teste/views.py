from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import folium
import geocoder
from django.db.models import Q

from .models import Search
from .models import department,employee, Car, Model
from users.models import Profile
from agence.models import Agence
from voiture.models import Voiture
from paiement.models import Paiement
from teste.models import Image


# Create your views here.
def map(request):
    #create Map objects
    if request.method == "POST":
        adresse = request.POST.get('adresse')
        donne = Search(adresse=adresse)
        donne.save()
        return redirect('map_location')
    else:    
        adresse = Search.objects.all().last()
        location = geocoder.osm(adresse)
        lat = location.lat
        lng = location.lng
        country = location.country
        if lat == None or lng == None:
            adresse.delete()
            return HttpResponse('You address input is invalid')

        m = folium.Map(location=[19, -12], zoom_start=2)
        #folium.Marker([5.594, -0.219], tooltip='Click for more', popup='Ghana').add_to(m)
        folium.Marker([lat, lng], tooltip='Click for more', popup=country).add_to(m)
        #GET HTML PRESENTATION OF MAP OBJECT
        m = m._repr_html_()
        context = {
                'm': m,
            }
        return render(request, 'teste/teste_map.html', context)

def calculate(request):
    return render(request, 'teste/multiforms.html')

def multiforms(request):
    return render(request, 'teste/multi-form.html')  

def disable_btn(request):
    return render(request, 'teste/disabled_btn.html')  

def getdata(request):
    template_name = 'teste/selectbox.html'
    #deptcontext = department.objects.all()
    #empcontext = employee.objects.all()
    agencePro = Agence.objects.all()
    agence = Agence.objects.all()
    agenceUser= Agence.objects.exclude(userLoueur__isnull=True)
    loueur = Profile.objects.exclude(user__isnull=True)
    #loueur = Profile.objects.all().exclude(user__isnull=True)
    context = {'empcontext':agencePro, 'loueur':loueur, 'agenceUser': agenceUser, 'agence': agence}
    return render(request,template_name,context)      

def main_view(request):
    #qs = Car.objects.all()
    qs = Profile.objects.all().exclude(user__isnull=True)
    context = {'qs': qs}
    return render(request, 'teste/teste_dropdown.html', context)  

def get_json_car_data(request):
    #qs_val = list(Car.objects.values())
    qs_val = list(Profile.objects.values())
    return JsonResponse({'data': qs_val})  

def get_json_model_data(request, *args, **kwargs):
    select_car = kwargs.get('car')
    #obje_model = list(Model.objects.filter(car__name=select_car).values())
    obje_model = list(Agence.objects.filter(username__user=select_car).values())
    return JsonResponse({'data': obje_model})


def simpleCheckout(request):
    #pay = Paiement.objects.all().order_by('-id')[:1]
    if 'search' in request.GET:
        q = request.GET['search']
        pay = Paiement.objects.filter(Q(__icontains=q))
    else:
        pay = Paiement.objects.all().order_by('-id')[:1]    
        context = {'paiement': pay}
        return render(request, 'teste/teste_paiement.html', context)    


def affichage(request):
    liste = Image.objects.all()
    return render(request, "teste/affichageImage.html", {"liste_vehi": liste})

