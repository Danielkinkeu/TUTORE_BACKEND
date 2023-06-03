from django.db import models
from django.contrib.auth.models import User
# Create your models here.
category=[
    ('epreuve','epreuve'),
    ('controle continu','controle continu'),
    ('session normale','session normale'),
    ('communiquer','communiquer'),
    ('emplois du temps','emplois du temps'),
]
class Document(models.Model):
    doc = models.FileField(default='')
    nom_doc  = models.CharField(max_length = 50,default='')
    date_creation = models.DateTimeField(auto_now=True)
    type_doc = models.CharField(max_length = 50,default='')
    description_doc = models.CharField(max_length = 255,default=' document administratif')
    category=models.CharField(max_length = 30,default="epreuve",choices=category)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    class Meta:
        ordering = ['-date_creation']
  