from django.urls import path

from site_data.views import SiteDataListView

urlpatterns = [
    path("list/site",SiteDataListView.as_view())
]


