import uuid

from django.db import models
from apps.property.models import Property
from apps.core.models import TimestampableMixin
from apps.core.models import DeletedMixin


class Advertisement(TimestampableMixin):
    advertisement_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=False)
    platform_name = models.CharField(max_length=100)
    platform_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'advertisement'
        ordering = ['-created_at']
        verbose_name = 'advertisement'
        verbose_name_plural = 'advertisements'

    def __str__(self):
        return f'{self.property}, {self.platform_name}'

