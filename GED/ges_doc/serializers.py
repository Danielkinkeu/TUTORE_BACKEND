# import serializers from the REST framework
from rest_framework import serializers
 
# import the todo data model
from .models import Document, Fichier

class adminSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Document
        fields = ('doc','nom_doc','date_creation', 'type_doc','description_doc','category','folder','user')
        
class fichierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fichier
        fields = ('nom','user')        