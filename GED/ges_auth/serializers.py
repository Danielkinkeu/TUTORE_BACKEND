from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _
from .models import *

# from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated
# from .models import Account
UserModel = get_user_model()
class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profils
        fields = ('photo', 'nom_utilisateur', 'user')
        
    # password = serializers.CharField(write_only=True, validators=[validate_password])

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password')
        
    password = serializers.CharField(write_only=True, validators=[validate_password])


# class LoginSerializer(serializers.Serializer):
#     class Meta:
#         model = UserModel
#         fields = ('email', 'password')
#     email = serializers.EmailField(max_length=255)
#     password = serializers.CharField(
#         label=_("Password"),
#         style={'input_type': 'password'},
#         trim_whitespace=False,
#         max_length=128,
#         write_only=True
#     )

#     def validate(self, data):
#         email = data.get('email')
#         password = data.get('password')
        
#         if email and password:
#             user = authenticate(request=self.context.get('request'),
#                 email=email, password=password)
#             print(password)
#             if not user:
#                 msg = _('Unable to log in with provided credentials.')
#                 raise serializers.ValidationError(msg, code='authorization')
#         else:
#             msg = _('Must include "email" and "password".')
#             raise serializers.ValidationError(msg, code='authorization')

#         data['user'] = user
#         return data

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class PasswordResetSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, validators=[validate_password])
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [ 'email', 'last_name']    