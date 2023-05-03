from django.urls import path
from paiement import views

urlpatterns = [
    path('mode_paiement/', views.mode_paiement, name="ac_paiement"),
    path('paiement/<str:pk>', views.ajout_paiement, name="paiement"),
    path('final_page/', views.final_page, name="final_page"),
    path('genere/<int:id>',views.generer, name="generer"),
    #path('preparation_pai/', views.preparation_pay, name="prepare_pay"),
    path('paiement_form/', views.paiement_form, name="pay_form"),
]