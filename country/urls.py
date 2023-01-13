from django.urls import path
from .views import CountryListView, CountryDetailView

urlpatterns = [
    path('', CountryListView.as_view(),),
    path('<int:pk>', CountryDetailView.as_view(),)
]