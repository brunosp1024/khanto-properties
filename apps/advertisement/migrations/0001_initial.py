# Generated by Django 4.2.5 on 2023-09-19 12:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Deleted at')),
                ('advertisement_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('platform_name', models.CharField(max_length=100)),
                ('platform_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
            ],
            options={
                'verbose_name': 'advertisement',
                'verbose_name_plural': 'advertisements',
                'db_table': 'advertisement',
                'ordering': ['-created_at'],
            },
        ),
    ]