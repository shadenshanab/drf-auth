from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers  import CountrySerializer

from .models import Country

from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerOrReadOnly

class CountryListView(ListCreateAPIView):
    queryset= Country.objects.all()
    serializer_class= CountrySerializer
    permission_classes= [IsAuthenticated]

class CountryDetailView(RetrieveUpdateDestroyAPIView):
    queryset= Country.objects.all()
    serializer_class= CountrySerializer
    permission_classes= [IsAuthenticated, IsOwnerOrReadOnly]