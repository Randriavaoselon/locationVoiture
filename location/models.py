from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from agence.models import Agence
from voiture.models import Voiture
import datetime

# Create your models here.
class Location(models.Model):
    nom_Client = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name="nom_Client")
    nom_Agence = models.ForeignKey(Agence, on_delete=models.CASCADE, related_name="nom_Agence", null=True)
    loueur = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="user_loueur", null=True)
    type_loc = models.CharField(max_length=50, null=True, default="Auccun")
    dt_demande = models.DateField(("Date"), default=datetime.date.today, null=True)
    destination = models.CharField(max_length=100, null=True, default="Auccun")
    autre_cond = models.CharField(max_length=10, null=True, default="Auccun")
    nom_autre = models.CharField(max_length=100, null=True, default="Auccun")
    email_autre = models.CharField(max_length=100, default="", null=True)
    cin_autre = models.PositiveIntegerField(default=0, null=True)
    permis_autre = models.CharField(max_length=13, null=True, default="Auccun")
    adresse_autre = models.CharField(max_length=100, null=True, default="Auccun")

    def __str__(self):
        return str(self.id)