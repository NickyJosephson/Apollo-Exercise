from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VehicleSerializer
from .models import Vehicle
import json.decoder

class CustomAPIView(APIView):
    def dispatch(self, request, *args, **kwargs):
        try:
            # Try parsing the request
            return super().dispatch(request, *args, **kwargs)
        except json.decoder.JSONDecodeError:
            # Handle invalid JSON globally
            return Response(
                {"error": "Invalid JSON format. Please send valid JSON."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Vehicle.DoesNotExist:
            return Response(
                {'errors': 'Vehicle not found.'},
            status=status.HTTP_404_NOT_FOUND
            ) 


class VehicleView(CustomAPIView):
    def get(self, request, vin=None):
        if vin:
            instance = Vehicle.objects.get(vin=vin)
            serializer = VehicleSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
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
        instance = Vehicle.objects.get(vin=vin)
        serializer = VehicleSerializer(instance, data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def delete(self, request, vin=None):
        vehicle = Vehicle.objects.get(vin=vin)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




    
    
