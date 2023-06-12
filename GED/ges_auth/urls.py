from django.urls import path
from ges_auth.views import *
from ges_auth import views

urlpatterns = [
    path('login',views.LoginView.as_view(), name='login'),   
    path('register',views.RegistrationView.as_view(), name='register'),      
    path('password_reset/', PasswordResetAPIView.as_view()),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmAPIView.as_view()),  
    path('create_profil', CreateProfilView.as_view()),
    path('update_profil', UpdateProfilView.as_view()),
    path('delete_profil', DeleteProfilView.as_view()),
    path('list_profil',ListProfilView.as_view(), name='profil'),
    path('profil',ProfilView.as_view(), name='monProfil'),
    path('filter-users/', FilterUsersView.as_view()),  
]