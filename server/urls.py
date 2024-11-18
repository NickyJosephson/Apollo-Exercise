from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('vehicle',views.VehicleView.as_view(), name='vehicle-list-post-get'),
    path('vehicle/<str:vin>',views.VehicleView.as_view(), name='vehicle-id-get-post-delete')
]