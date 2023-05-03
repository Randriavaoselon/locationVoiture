from django.urls import path
from voiture import views

urlpatterns = [
    path('acceuil_reservation/', views.acceuil_reservation, name="acceuil"),
    #path('reservation/<str:pk>', views.reservation, name="voiture"),
    path('ajout_vehicule/', views.ajout_vehicule, name="ajout_vehicule"),
    #path('liste_vehicule/', views.liste_vehicule, name="liste_vehicule"),

    path('detail_vehicule/<str:pk>', views.detail_vehicule, name="details_vehicule"),
    path('reserve_vehicule/<str:pk>', views.reserve_vehicule, name="voiture"),

    path('voitureListe/', views.liste_voiture, name="liste")
]