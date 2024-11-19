# Vehicle Management API

A Django REST Framework-based API for managing vehicle information. This project provides endpoints to create, retrieve, update, and delete vehicle records, complete with validation and error handling.

---

## **Table of Contents**

1. [Features](#features)
2. [Technologies](#technologies)
3. [Setup and Installation](#setup-and-installation)
4. [Usage](#usage)
   - [Endpoints](#endpoints)
   - [Sample Requests](#sample-requests)
5. [Testing](#testing)

---

## **Features**

- Add new vehicles with detailed specifications.
- Retrieve all vehicles or specific ones by VIN.
- Update existing vehicle details.
- Delete vehicles by VIN.
- Error handling for validation, missing records, and malformed requests.

---

## **Technologies**

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default, can be replaced with PostgreSQL or others)
- **Testing**: Django Test Framework
---

## **Setup and Installation**

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:NickyJosephson/Apollo-Exercise.git
   cd ApolloExcercise
2. **Create a virtual environment, and install the required dependencies**;
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    pip install -r requirements.txt
3. **Apply the database migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
4. **Run the server**
    ```bash
    python manage.py runserver
5. **Alternatively, you can use the provided makefile to do the installation for you**
    ```bash
    make setup
---


## **Usage**
### Endpoints

| Method | Endpoint        | Description                           |
|--------|------------------|---------------------------------------|
| GET    | `/vehicle`      | Retrieve a list of all vehicles.      |
| GET    | `/vehicle/<vin>`| Retrieve a single vehicle by VIN.     |
| POST   | `/vehicle`      | Create a new vehicle.                 |
| PUT    | `/vehicle/<vin>`| Update an existing vehicle by VIN.    |
| DELETE | `/vehicle/<vin>`| Delete a vehicle by VIN.              |
| GET    | `/sold-vehicles`      | Retrieve a list of all sold vehicles.      |
| GET    | `/sold-vehicles/<vin>`| Retrieve a single sold vehicle by VIN.     |
| POST   | `/sold-vehicles`      | Create a new sold vehicle, remove it from the vehicles table                |
| PUT    | `/sold-vehicles/<vin>`| Update an existing sold vehicle by VIN.    |
| DELETE | `/sold-vehicles/<vin>`| Delete a sold vehicle by VIN.              |

### Sample Requests
1. ```bash
    {
        "vin": "1HGCM82633A123456",
        "manufacturer_name": "Honda",
        "description": "A reliable sedan.",
        "horse_power": 158,
        "model_name": "Civic",
        "model_year": "2020-05-01",
        "purchase_price": 22000.50,
        "fuel_type": "Gasoline"
    }


## **Testing**

1. Simply run this command to go through the test suite
    ```bash
    python manage.py test
