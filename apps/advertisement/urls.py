from apps.advertisement.views import AdvertisementViewSet
from rest_framework.routers import DefaultRouter

app_name = 'advertisement'

class OptionalSlashRouter(DefaultRouter):
    def __init__(self):
        super().__init__()
        self.trailing_slash = '/?'

router = OptionalSlashRouter()
router.register(r'advertisements', AdvertisementViewSet)

urlpatterns = router.urls