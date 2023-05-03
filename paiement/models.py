from django.db import models
from location.models import Location
from users.models import Profile
import datetime

# Create your models here.
class Paiement(models.Model):
    id_loc = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, related_name="id_loc")
    num_compte = models.PositiveIntegerField(default=0, null=True)
    total = models.FloatField()
    date_pay = models.DateTimeField(default=datetime.datetime.now())
    loueurUser = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="userloueur", null=True)

    def __str__(self):
        return str(self.id) 