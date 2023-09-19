from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ Implements actions to advertisement: list, create, retrieve e update """

    serializer_class = AdvertisementSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Advertisement.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch']
