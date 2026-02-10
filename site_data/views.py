from drf_spectacular.utils import extend_schema
from rest_framework import generics

from site_data.models import SiteDate
from site_data.serizlizers import SiteDataModelSerializers

@extend_schema(tags=["site"])
class SiteDataListView(generics.ListAPIView):
    queryset = SiteDate.objects.all()
    serializer_class = SiteDataModelSerializers