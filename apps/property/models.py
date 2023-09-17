import uuid

from django.db import models

from apps.core.models import TimestampableMixin
from apps.core.models import DeletedMixin


class Property(TimestampableMixin, DeletedMixin):
    property_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property_code = models.CharField(max_length=10, unique=True)
    guest_limit = models.PositiveIntegerField(default=1)
    bathroom_count = models.PositiveIntegerField(null=True, blank=True, default=0)
    pets_allowed = models.BooleanField(default=True)
    cleaning_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.0)
    activation_date = models.DateField()

    class Meta:
        db_table = 'property'
        ordering = ['property_code']
        verbose_name = 'property'
        verbose_name_plural = 'properties'

    def __str__(self):
        return f'{self.property_code}, {self.guest_limit}, {self.bathroom_count}'
