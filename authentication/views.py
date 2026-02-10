from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.models import User
from authentication.serializers import UserModelSerializer




@extend_schema(tags=["register"])
class RegisterCreateApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer



@extend_schema(tags=["login"])
class CustomTokenObtainPairView(TokenObtainPairView):
    pass

@extend_schema(tags=["login"])
class CustomTokenRefreshView(TokenRefreshView):
    pass