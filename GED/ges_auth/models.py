from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profils(models.Model):
    # code_utilisateur = models.CharField(max_length=50,default='')
    photo = models.ImageField(default='')
    nom_utilisateur  = models.CharField(max_length = 30,default='')
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    
    
    
    
# class Utilisateurs(models.Model):
#     code = models.CharField(max_length=50,default='')
#     nom  = models.CharField(max_length = 30,default='')
#     motdepasse = models.CharField(max_length = 30,default='')
    