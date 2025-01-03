from django.db import models
from django.core.validators import RegexValidator
from django.db.models import UniqueConstraint
import re

# Create your models here.
class Vehicle(models.Model):
    vin = models.CharField(
        primary_key=True, 
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-HJ-NPR-Z0-9]{17}$',
                message="Invalid VIN format.",
                flags=re.IGNORECASE,
            )
        ],  
        max_length=128    
    )
    manufacturer_name = models.CharField(blank=False, max_length=128)
    description = models.TextField(blank=False, null=False)
    horse_power = models.IntegerField(blank=False, null=False)
    model_name = models.CharField(blank=False, null=False, max_length=128)
    model_year = models.IntegerField(blank=False, null=False)
    purchase_price = models.FloatField(blank=False, null=False)
    fuel_type = models.CharField(blank=False, null=False, max_length=128)
    color = models.CharField(blank=False, null=False, max_length=128)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['vin'],
                name='unique_vin_case_insensitive',
                violation_error_message="VIN must be unique (case-insensitive)."
            )
        ]

class SoldVehicles(models.Model):
    vin = models.CharField(
    primary_key=True, 
    unique=True,
    validators=[
        RegexValidator(
            regex=r'^[A-HJ-NPR-Z0-9]{17}$',
            message="Invalid VIN format.",
            flags=re.IGNORECASE,
        )
    ],  
    max_length=128    
    )
    manufacturer_name = models.CharField(blank=False, max_length=128)
    description = models.TextField(blank=False, null=False)
    horse_power = models.IntegerField(blank=False, null=False)
    model_name = models.CharField(blank=False, null=False, max_length=128)
    model_year = models.IntegerField(blank=False, null=False)
    purchase_price = models.FloatField(blank=False, null=False)
    fuel_type = models.CharField(blank=False, null=False, max_length=128)
    color = models.CharField(blank=False, null=False, max_length=128)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['vin'],
                name='unique_vin_case_insensitive_sold_vehicle',
                violation_error_message="VIN must be unique (case-insensitive)."
            )
        ]