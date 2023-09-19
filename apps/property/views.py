from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Property
from .serializers import PropertySerializer


class PropertyViewSet(ModelViewSet):
    """ Implements all actions to properties: list, create, retrieve, update e delete """

    serializer_class = PropertySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Property.objects.all()
