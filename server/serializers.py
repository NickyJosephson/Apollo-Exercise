from rest_framework import serializers

from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            'vin',
            'manufacturer_name',
            'description',
            'horse_power',
            'model_name',
            'model_year',
            'purchase_price',
            'fuel_type'
        ]
        
    def validate_vin(self, value):
        return value.upper()
