from django.urls import path
from location import views

urlpatterns = [
    path('acceuil_demande_location/', views.acceuil_demande_location, name="a_demande_loc"),
    path('envoie_demande/<str:pk>', views.envoie_demande, name="envoie_demande"),
    path('procedure/', views.procedure, name="procedure"),
    path('impression/<int:id>',views.imprimerAgence, name="impression"),
    #path('confirm_loc/', views.nb_location, name="confirm_loc")
]