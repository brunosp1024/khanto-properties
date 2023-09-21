from apps.property.views import PropertyViewSet
from rest_framework.routers import DefaultRouter

app_name = 'property'

class OptionalSlashRouter(DefaultRouter):
    def __init__(self):
        super().__init__()
        self.trailing_slash = '/?'

router = OptionalSlashRouter()
router.register(r'properties', PropertyViewSet)

urlpatterns = router.urls