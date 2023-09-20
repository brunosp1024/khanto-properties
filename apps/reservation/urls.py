from apps.reservation.views import ReservationViewSet
from rest_framework import routers

app_name = 'reservation'

router = routers.DefaultRouter()
router.register(r'reservations', ReservationViewSet)

urlpatterns = router.urls