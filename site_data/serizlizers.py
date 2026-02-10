from rest_framework import serializers

from site_data.models import SiteDate


class SiteDataModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = SiteDate
        fields = '__all__'
