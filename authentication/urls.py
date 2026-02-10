from django.contrib import admin
from django.urls import path

from authentication.views import RegisterCreateApiView, CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path("/register/", RegisterCreateApiView.as_view()),
]

# JWT
urlpatterns += [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]