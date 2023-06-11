from django.shortcuts import render

# Create your views here.
from base64 import urlsafe_b64encode
from django.conf import settings
from django.http import JsonResponse
from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, get_user_model, login
from rest_framework.generics import RetrieveAPIView
# import utils.response_handler as rh
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer, LoginSerializer, PasswordResetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User, update_last_login
from rest_framework.authtoken.models import Token
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from rest_framework.generics import  CreateAPIView, UpdateAPIView, DestroyAPIView
from ges_auth.models import CustomUser


# UserModel = get_user_model()
class RegistrationView(APIView):
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        username = request.data.get('username')
        print(email)
        print(password)
        print(username)
        if not email or not password or not username:
            return Response({'error': 'Veuillez fournir les informations nécessaires pour l\'enregistrement'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = CustomUser.objects.create_user(username, email, password)
            user.save()
        return Response({'success': 'Utilisateur enregistré avec succès'}, status=status.HTTP_201_CREATED)
        # except:
        #     return Response({'error': 'Une erreur s\'est produite lors de l\'enregistrement de l\'utilisateur'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    



# class LoginView(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = LoginSerializer
#     def post(self, request, *args, **kwargs):
#         serializer = LoginSerializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         update_last_login(None, user)
        
#         # token, created = User.objects.get_or_create(user=user)
#         return Response({'success': 'Utilisateur connecté avec succès'}, status=status.HTTP_200_OK)
        
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(request, email=serializer.validated_data['email'], password=serializer.validated_data['password'])

        if user is not None:
            login(request, user)
            
        else:
            return Response({"detail": "Invalid email/password pair"}, status=status.HTTP_401_UNAUTHORIZED)

        user_info = CustomUser.objects.get(email=user.email)
        data = {'username': user_info.first_name, 'email': user_info.email}
        return Response({'success': 'Utilisateur connecté avec succès', 'data': data}, status=status.HTTP_200_OK)
        

class PasswordResetAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        email = serializer.validated_data['email']
        user_queryset = UserModel.objects.filter(username=username, email=email)
        if not user_queryset.exists():
            return Response({'detail': 'Invalid phone number or email.'}, status=status.HTTP_400_BAD_REQUEST)

        user = user_queryset.first()
        uid = urlsafe_b64encode(force_bytes(user.pk)).decode('utf-8')
        token = default_token_generator.make_token(user)
        reset_url = f"{request.get_host()}/api/auth/password_reset_confirm/{uid}/{token}"
        message = f"Hello {user.username},\n\nPlease reset your password by clicking on the link: {reset_url}\n\nBest regards,\nThe KapyGenius Team"

        send_mail(
            subject="Reset your password",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False
        )

        return Response({'detail': f'Password reset link has been sent to {email}.'}, status=status.HTTP_204_NO_CONTENT)


class PasswordResetConfirmAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordResetSerializer

    def post(self, request, uidb64, token):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = UserModel.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            new_password = serializer.validated_data['password']
            user.set_password(new_password)
            user.save()
            return Response({'detail': 'Your password has been reset.'}, status=status.HTTP_204_NO_CONTENT)

        return Response({'detail': 'Invalid reset link.'}, status=status.HTTP_400_BAD_REQUEST)
    

class CreateProfilView(CreateAPIView):
    queryset= Profils.objects.all()
    serializer_class= ProfilSerializer
    
class UpdateProfilView(UpdateAPIView): 
    queryset= Profils.objects.all()
    serializer_class= ProfilSerializer

class DeleteProfilView(DestroyAPIView):
    queryset= Profils.objects.all()
    serializer_class= ProfilSerializer
    
    
class FilterUsersView(View):
    def get(self, request):
        email = request.GET.get('email')
        users = CustomUser.objects.filter(email=email)
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)    