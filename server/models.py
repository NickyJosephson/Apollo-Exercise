from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Vehicle(models.Model):
    vin = models.CharField(
        primary_key=True, 
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-HJ-NPR-Z0-9]{17}$',  # VIN format (17 alphanumeric, excluding I, O, Q)
                message="Invalid VIN format."
            )
        ],  
        max_length=128    
    )
    manufacturer_name = models.CharField(blank=False, max_length=128)
    description = models.TextField(blank=False, null=False)
    horse_power = models.IntegerField(blank=False, null=False)
    model_name = models.CharField(blank=False, null=False, max_length=128)
    model_year = models.DateField(blank=False, null=False)
    purchase_price = models.FloatField(blank=False, null=False)
    fuel_type = models.CharField(blank=False, null=False, max_length=128)