from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from authentication.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "email","password"
    def validate_password(self, password):
          password = make_password(password)
          return password

