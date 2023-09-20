import uuid

from django.db import models

from apps.advertisement.models import Advertisement
from apps.core.models import DeletedMixin
from apps.core.models import TimestampableMixin
from apps.core.utils.functions_utils import generate_random_code


class Reservation(TimestampableMixin, DeletedMixin):
    reservation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    reservation_code = models.CharField(
        max_length=100, default=generate_random_code, unique=True, editable=False
    )
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(null=True, blank=True)
    num_guests = models.PositiveIntegerField()

    class Meta:
        db_table = 'reservation'
        ordering = ['reservation_code']
        verbose_name = 'reservation'
        verbose_name_plural = 'reservations'

    def __str__(self):
        return f'{self.reservation_code}, {self.advertisement}'
