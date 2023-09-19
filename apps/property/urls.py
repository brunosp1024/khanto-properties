from apps.property.views import PropertyViewSet
from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'properties', PropertyViewSet)

urlpatterns = router.urls