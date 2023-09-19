from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# swagger documentation
schema_view = get_schema_view(
   openapi.Info(
      title="Khanto properties API",
      default_version='v1',
      description="property listing and your booking",
      terms_of_service="#",
      contact=openapi.Contact(email="bruno.tech@seazone.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.property.urls', namespace='api')),
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
