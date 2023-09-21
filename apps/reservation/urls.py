from apps.reservation.views import ReservationViewSet
from rest_framework.routers import DefaultRouter

app_name = 'reservation'

class OptionalSlashRouter(DefaultRouter):
    def __init__(self):
        super().__init__()
        self.trailing_slash = '/?'

router = OptionalSlashRouter()
router.register(r'reservations', ReservationViewSet)

urlpatterns = router.urls