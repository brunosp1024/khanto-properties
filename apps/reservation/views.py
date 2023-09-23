from dateutil import parser

from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.advertisement.models import Advertisement

from .models import Reservation
from .serializers import ReservationSerializer


class ReservationViewSet(ModelViewSet):
    """ Implements actions to reservations: list, create, retrieve e delete """

    serializer_class = ReservationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    http_method_names = ['get', 'post', 'delete']

    def create(self, request):
        try:
            advertisement = Advertisement.objects.get(pk=request.data['advertisement'])
            check_in = parser.parse(request.data['check_in_date'])
            check_out = parser.parse(request.data['check_out_date'])

            has_conflicting_reservations = Reservation.objects.filter(
                advertisement__property=advertisement.property,
                check_out_date__gt=check_in
            ).exists()

            if has_conflicting_reservations:
                return Response(
                    {'message': 'There is already a reservation for this property.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if check_in > check_out:
                return Response(
                    {'message': 'Check-in cannot be later than check-out'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as ex:
            return Response(
                    {'message': f'Failed to create reservation. Error: {ex}'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        return super().create(request)
