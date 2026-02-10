from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include
from frontend.view import index, register_page
urlpatterns = [
    path("", include("frontend.urls")),
    path("api/v1/register/", register_page, name="frontend_register"),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

urlpatterns +=[
    path('admin/', admin.site.urls),
    path("api/v1/",include("authentication.urls")),
    path("api/v2/", include("site_data.urls")),
    path("api/v3/", include("home.urls")),
]

