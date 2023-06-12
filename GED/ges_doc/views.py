from .models import Document
# api 
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import viewsets
# import the userSerializer from the serializer file
from .serializers import *
from rest_framework.decorators import api_view
# import the user model from the models file
from .models import Document, Fichier
from rest_framework.response import Response
# create a class for the user model viewsets

    
class adminView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the userSerializer class
    serializer_class = adminSerializer
 
    # define a variable and populate it
    # with the user objects
    queryset = Document.objects.all()
    
# class ListDocumentView(ListAPIView):
#     queryset= Document.objects.all()
#     serializer_class= adminSerializer
class ListDocumentView(ListAPIView):
    serializer_class = adminSerializer

    def get_queryset(self):
        queryset = Document.objects.all()
        nom_doc = self.request.query_params.get('nom_doc')
        if nom_doc is not None:
            queryset = queryset.filter(nom_doc__icontains=nom_doc)
        return queryset    

class CreateDocumentView(CreateAPIView):
    queryset= Document.objects.all()
    serializer_class= adminSerializer
    
class UpdateDocumentView(UpdateAPIView): 
    queryset= Document.objects.all()
    serializer_class= adminSerializer

class DeleteDocumentView(DestroyAPIView):
    queryset= Document.objects.all()
    serializer_class= adminSerializer
    
    
class ListFichierView(ListAPIView):
    queryset= Fichier.objects.all()
    serializer_class= fichierSerializer

class CreateFichierView(CreateAPIView):
    queryset= Fichier.objects.all()
    serializer_class= fichierSerializer
    
class UpdateFichierView(UpdateAPIView): 
    queryset= Fichier.objects.all()
    serializer_class= fichierSerializer

class DeleteFichierView(DestroyAPIView):
    queryset= Fichier.objects.all()
    serializer_class= fichierSerializer    