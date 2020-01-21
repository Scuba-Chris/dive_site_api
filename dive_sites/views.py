from .serializers import DiveSiteSerializer
from .models import DiveSite
from rest_framework import generics

class DiveSiteList(generics.ListCreateAPIView):
    queryset = DiveSite.objects.all()
    serializer_class = DiveSiteSerializer

class DiveSiteDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiveSite.objects.all()
    serializer_class = DiveSiteSerializer


