from apps.advertisement.views import AdvertisementViewSet
from rest_framework import routers

app_name = 'advertisement'

router = routers.DefaultRouter()
router.register(r'advertisements', AdvertisementViewSet)

urlpatterns = router.urls