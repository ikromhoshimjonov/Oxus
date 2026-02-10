from django.contrib import admin

from authentication.models import User
from home.models import Home, ImageHome, City
from site_data.models import SiteDate


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(SiteDate)
class SiteAdmin(admin.ModelAdmin):
    pass

@admin.register(ImageHome)
class ImageSiteAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
