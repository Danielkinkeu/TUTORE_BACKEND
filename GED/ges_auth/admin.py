from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Profils)
admin.site.register(CustomUser)
# admin.site.register(CustomUserManager)