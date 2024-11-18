from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VehicleSerializer
from .models import Vehicle

class VehicleView(APIView):
    def get(self, request, vin=None):
        try:
            if vin:
                instance = Vehicle.objects.get(vin=vin)
                serializer = VehicleSerializer(instance)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                queryset = Vehicle.objects.all()
                serializer = VehicleSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Vehicle.DoesNotExist:
            return Response({'errors': 'Vehicle not found.'}, status=status.HTTP_404_NOT_FOUND)   
        except Exception as e:
            raise e
            
    
    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            raise e
        
    def put(self, request, vin=None):
        try:
            instance = Vehicle.objects.get(vin=vin)
            serializer = VehicleSerializer(instance, data=request.data)
            if serializer.is_valid():
                instance = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Vehicle.DoesNotExist:
            return Response({'errors': 'Vehicle not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            raise e
    
    def delete(self, request, vin=None):
        try:
            vehicle = Vehicle.objects.get(vin=vin)
            vehicle.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vehicle.DoesNotExist:
            return Response({'detail': 'Vehicle not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            raise e




    
    
