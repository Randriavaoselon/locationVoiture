from django.urls import path
from teste import views

urlpatterns = [
    path('map_location/', views.map, name="map_location"),

    path('duree/', views.calculate, name="duree"),
    path('multiform/', views.multiforms, name="form"),
    path('disable/', views.disable_btn, name="btn"),
    path('select/', views.getdata, name="select"),
    
    path('drop/', views.main_view, name="drop"),
    path('car-json/', views.get_json_car_data, name="car-json"),
    path('model-json/<str:car>/', views.get_json_model_data, name="model-json"),

    path('teste_paiement/', views.simpleCheckout, name="teste_paiement"),

    path('image/', views.affichage, name="affichage")
]