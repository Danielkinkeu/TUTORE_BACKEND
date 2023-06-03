from django.urls import path, include, re_path

from GED.settings import DEBUG,STATIC_ROOT,MEDIA_ROOT, MEDIA_URL, STATIC_URL
from django.conf.urls.static import static 
# from ges_auth.views import *
from .views import *
from ges_doc import views

# import routers from the REST framework
# it is necessary for routing
from rest_framework import routers
# create a router object
router = routers.DefaultRouter()
 
# register the router
router.register(r'adminDocument',views.adminView, 'task')



urlpatterns = [
    path('', include(router.urls)),

    path('list_document',views.ListDocumentView.as_view(), name='document'),
    path('add_document/',views.CreateDocumentView.as_view(), name='create_document'),
    path('<pk>/update_document/',views.UpdateDocumentView.as_view(), name='document_update'),
    path('<pk>/delete_document/',views.DeleteDocumentView.as_view(), name='document_delete'),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)




