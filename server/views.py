from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VehicleSerializer, SoldVehicleSerializer
from .models import Vehicle, SoldVehicles
import json.decoder

class CustomAPIView(APIView):
    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except json.decoder.JSONDecodeError:
            return Response(
                {"error": "Invalid JSON format. Please send valid JSON."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            print(e)
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class VehicleView(CustomAPIView):
    def get(self, request, vin=None):
        if vin:
            try:
                instance = Vehicle.objects.get(vin=vin.upper())
                serializer = VehicleSerializer(instance)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Vehicle.DoesNotExist:
                return Response(
                    {'errors': 'Vehicle not found.'},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            queryset = Vehicle.objects.all()
            serializer = VehicleSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def put(self, request, vin=None):
        try:
            instance = Vehicle.objects.get(vin=vin.upper())
            serializer = VehicleSerializer(instance, data=request.data)
            if serializer.is_valid():
                instance = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Vehicle.DoesNotExist:
            return Response(
                {'errors': 'Vehicle not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def delete(self, request, vin=None):
        try:
            vehicle = Vehicle.objects.get(vin=vin.upper())
            vehicle.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vehicle.DoesNotExist:
            return Response(
                {'errors': 'Vehicle not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        


class SoldVehicleView(CustomAPIView):
    def get(self, request, vin=None):
        if vin:
            try:
                instance = SoldVehicles.objects.get(vin=vin.upper())
                serializer = SoldVehicleSerializer(instance)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except SoldVehicles.DoesNotExist:
                return Response(
                    {'errors': 'Vehicle not found.'},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            queryset = SoldVehicles.objects.all()
            serializer = VehicleSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, vin=None):
        existing_instance = Vehicle.objects.get(vin=request.data['vin'].upper())
        print('deleting existing record')
        existing_instance.delete()
        serializer = SoldVehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('record added to new table')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def put(self, request, vin=None):
        try:
            instance = SoldVehicles.objects.get(vin=vin.upper())
            serializer = SoldVehicleSerializer(instance, data=request.data)
            if serializer.is_valid():
                instance = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except SoldVehicles.DoesNotExist:
            return Response(
                {'errors': 'Vehicle not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def delete(self, request, vin=None):
        try:
            vehicle = SoldVehicles.objects.get(vin=vin.upper())
            vehicle.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SoldVehicles.DoesNotExist:
            return Response(
                {'errors': 'Vehicle not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        