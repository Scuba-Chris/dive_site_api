from django.urls import path
from .views import DiveSiteList, DiveSiteDetails

urlpatterns = [
    path('dive_sites/', DiveSiteList.as_view(), name='dive_site_list'),
    path('dive_sites/<int:pk>', DiveSiteDetails.as_view(), name='dive_site_details')
]