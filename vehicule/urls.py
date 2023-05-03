from django.urls import path
from vehicule import views

urlpatterns = [
    path('list_voiture/', views.liste_vehicule, name="liste"),
    path('acceuil_reservation/', views.acceuil_reservation, name="acceuil"),
    #path('reservation/<str:pk>', views.reservation, name="voiture"),
    path('ajout_vehicule/', views.ajout_vehicule, name="ajout_vehicule"),
    path('detail_vehicule/<str:pk>', views.detail_vehicule, name="details_vehicule"),
    path('reserve_vehicule/<str:pk>', views.reserve_vehicule, name="voiture")
]