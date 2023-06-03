# import serializers from the REST framework
from rest_framework import serializers
 
# import the todo data model
from .models import Document

class adminSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Document
        fields = ('doc','nom_doc','date_creation', 'type_doc','description_doc','category','user')