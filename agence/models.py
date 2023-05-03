from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
#from users.models import Profile

# Create your models here.
class Agence(models.Model):
    userLoueur = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="loueurAgence", null=True)
    nom_agence = models.CharField(max_length=100, null=True)
    adresse_agence = models.CharField(max_length=100, null=True)
    tel_agence = models.PositiveIntegerField()
    email_agence = models.EmailField()
    fax_agence = models.CharField(max_length=100, null=True)

    def __str__(self):
       return self.nom_agence
    
    class Meta:
        db_table="agence"