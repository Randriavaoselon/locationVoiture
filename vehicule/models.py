from django.db import models
from users.models import Profile
from PIL import Image
import datetime

# Create your models here.

class Vehicule(models.Model):
    numSerie = models.IntegerField(null=True, default=0)
    numImm = models.CharField(max_length=10, null=True, default="")
    dateMiseEnCirc = models.DateField(("Date"), default=datetime.date.today, null=True)
    kilometrage = models.CharField(max_length=10, null=True, default="")
    date_reservetion = models.DateField(("Date"), default=datetime.date.today, null=True)
    dt_debut = models.DateField(("Date"), default=datetime.date.today, null=True)
    dt_fin = models.DateField(("Date"), default=datetime.date.today, null=True)
    type_vehicule = models.CharField(max_length=50, null=True, default="")
    jours = models.PositiveIntegerField(default=0)
    #kilometre = models.CharField(max_length=10, null=True, default="")
    marque_vehicule = models.CharField(max_length=50, null=True, default="")
    #nb_vehicule = models.PositiveIntegerField(default=0, null=True)
    type_prix = models.CharField(max_length=50, null=True, default="")
    prixJ = models.PositiveIntegerField(default=0)
    #prixKm = models.PositiveIntegerField(default=0)
    montant_total = models.PositiveIntegerField(default=0)
    condition = models.CharField(max_length=20, null=True, default="")
    #id_location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True, related_name='id_location')
    client_loueur = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="usr_loueur", null=True)
    photos = models.ImageField(upload_to="photos/%y")

    def __str__(self):
        return self.type_vehicule