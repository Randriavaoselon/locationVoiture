from django.urls import path
from users import views
from .views import home, profile, RegisterView


urlpatterns = [
    path('', views.home_loueur, name="home_loueur"),
    path('acceuil_inscription/', views.acceuil_inscription, name="a_inscription"),
    path('home/', views.home, name='users-home'),
    path('inscription/', views.inscription, name="inscription"),
    path('contact/', views.contact, name="contact"),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='profile'),

    # Chartjs progress bar
    path('cycle_paiemnt/', views.pay_reservation, name="cycle_pay"),
    path('location_paiement/', views.demande_pay, name="loc_paiement"),

    # Modification
    path('edite_location/<str:pk>', views.modification, name="edite_loc"),
    path('edite_reservation/<str:pk>', views.modification_reservation, name="edite_reserve"),

    # Suppression
    path('supprime/<str:pk>', views.suppression, name='supprime'),
    path('supprime_reservation/<str:pk>', views.suppression_reservation, name='supprime_reservation'),
    path('supprime_paiement/<str:pk>', views.suppression_paiement, name='supprime_paiement'),

    # Map
    path('mapDirection/', views.map_direction, name="map"),

    # Detail de client
    path('detail_client/<str:pk>', views.detail_client, name="details"),

    #page not found
    path('page_not_found/', views.page_not_found, name="not_found"),
]

