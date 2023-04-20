from rest_framework import viewsets

from .serializers import CatSerializer, OwnerSerializer
from .models import Cat, Owner


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer 



