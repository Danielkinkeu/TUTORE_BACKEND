from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
from django.db import models
from django.http import JsonResponse
from django.views import View
# from django.contrib.auth.models import User
# Create your models here.

    
    
class CustomUserManager(BaseUserManager):
    # def create_user(self, email, password=None, **extra_fields):
    #     if not email:
    #         raise ValueError('The Email must be set')
    #     email = self.normalize_email(email)
    #     user = self.model(email=email, **extra_fields)
    #     user.set_password(password)
    #     user.save()
    #     return user
    
    def create_user(self, email, password=None, name=None, **extra_fields):
        # print(email)
        # print(password)
        # print(name)
        nam = email
        if not password:
            raise ValueError('The Email must be set')
        email = self.normalize_email(password)
        user = self.model(email=password, **extra_fields)
        user.set_password(name)
        if name:
            user.first_name  = nam
        user.save()
        # print(user.email)
        # print(user.password)
        # print(user.first_name)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_staff
    
class Profils(models.Model):
    # code_utilisateur = models.CharField(max_length=50,default='')
    photo = models.ImageField(default='')
    nom_utilisateur  = models.CharField(max_length = 30,default='', unique=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)    
# class Utilisateurs(models.Model):
#     code = models.CharField(max_length=50,default='')
#     nom  = models.CharField(max_length = 30,default='')
#     motdepasse = models.CharField(max_length = 30,default='')

# class FilterUsersView(View):
#     def get(self, request):
#         email = request.GET.get('email')
#         users = CustomUser.objects.filter(email=email)
#         data = [user.to_dict() for user in users]
#         return JsonResponse(data, safe=False)    