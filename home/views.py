from drf_spectacular.utils import extend_schema
from rest_framework import generics
from home.models import Home
from home.serializers import HomeModelSerializer



@extend_schema(tags=["home"],summary="Uy malumotlari")
class HomeListApiView(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeModelSerializer