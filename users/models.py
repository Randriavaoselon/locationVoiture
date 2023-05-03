from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nom = models.CharField(max_length=100, null=True, default="")
    email = models.EmailField(default="", null=True)
    date_nais = models.DateField(("Date"), default=datetime.date.today, null=True)
    tel = models.CharField(max_length=10, null=True, default="")
    ville = models.CharField(max_length=50, null=True, default="")
    adresse = models.CharField(max_length=100, null=True, default="")
    cins = models.CharField(max_length=12, null=True, default="")
    nation = models.CharField(max_length=50, null=True, default="")
    cd_poste = models.PositiveIntegerField(default=0, null=True)
    num_permis = models.CharField(max_length=10, null=True, default="")
    sex = models.CharField(max_length=5, default="", null=True)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')

    def __str__(self):
         return self.nom
        #return f'{self.nom}' - {self.user.user}

    class Meta:
        db_table="client"    

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
