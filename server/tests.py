from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Vehicle

class VehicleViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.test_vehicle = Vehicle.objects.create(
            vin="1HGCM82633A123456",
            manufacturer_name="Honda",
            description="A reliable sedan.",
            horse_power=158,
            model_name="Civic",
            model_year=2020,
            purchase_price=22000.50,
            fuel_type="Gasoline"
        )

        self.valid_payload = {
            "vin": "1HGCM82633A123457",
            "manufacturer_name": "Toyota",
            "description": "A dependable car.",
            "horse_power": 200,
            "model_name": "Corolla",
            "model_year": 2021,
            "purchase_price": 24000.00,
            "fuel_type": "Gasoline"
        }

        self.invalid_payload = {
            "vin": "",
            "manufacturer_name": "Toyota",
            "description": "",
            "horse_power": -1,
            "model_name": "Corolla",
            "model_year": "invalid",
            "purchase_price": "invalid-price",
            "fuel_type": ""
        }

    def test_get_all_vehicles(self):
        response = self.client.get("/vehicle")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_vehicle_valid_vin(self):
        response = self.client.get(f"/vehicle/{self.test_vehicle.vin}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["vin"], self.test_vehicle.vin)

    def test_get_single_vehicle_invalid_vin(self):
        response = self.client.get("/vehicle/INVALIDVIN")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_vehicle_valid_payload(self):
        response = self.client.post("/vehicle", data=self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["vin"], self.valid_payload["vin"])

    def test_create_vehicle_invalid_payload(self):
        response = self.client.post("/vehicle", data=self.invalid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_update_vehicle_valid_payload(self):
        update_payload = {
            "vin": self.test_vehicle.vin,
            "manufacturer_name": "Honda",
            "description": "An updated description.",
            "horse_power": 160,
            "model_name": "Civic",
            "model_year": 2020,
            "purchase_price": 23000.00,
            "fuel_type": "Gasoline"
        }
        response = self.client.put(f"/vehicle/{self.test_vehicle.vin}", data=update_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], "An updated description.")

    def test_update_vehicle_invalid_payload(self):
        response = self.client.put(f"/vehicle/{self.test_vehicle.vin}", data=self.invalid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_delete_vehicle_valid_vin(self):
        response = self.client.delete(f"/vehicle/{self.test_vehicle.vin}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_vehicle_invalid_vin(self):
        response = self.client.delete("/vehicle/INVALIDVIN")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)