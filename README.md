# WaziTrack Backend

WaziTrack Backend is the backend system developed using Django and Django REST Framework with PostgreSQL as the database. This system provides API endpoints for user registration (farmers and companies), authentication via JWT, OTP verification, and more.

## Getting Started

To run this project locally, follow these steps:

### Prerequisites
Ensure you have Python, PostgreSQL, and pip installed on your machine.

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/WaziTrack-Backend.git
```

### 2. Navigate to the Project Directory

```bash
cd WaziTrack-Backend
```

### 3. Create and Activate a Virtual Environment

You can create a virtual environment named `sense` (or any other name of your choice):

```bash
python -m venv sense  # "sense" is the virtual environment name used here.
```

For Windows, activate the environment using:

```bash
.\sense\Scripts\activate
```

For macOS/Linux:

```bash
source sense/bin/activate
```

### 4. Install Dependencies

Once the virtual environment is activated, install the project dependencies:

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a `.env` file in the project root and define the following environment variables:

```
DB_NAME=<YourDatabaseName>
DB_USER=<YourDatabaseUser>
DB_PWD=<YourDatabasePassword>
DB_HOST=<YourDatabaseHost>
DB_PORT=5432
```

### 6. Set Up the Database

After configuring your `.env` file with your database settings, apply migrations to set up your database schema:

```bash
python manage.py migrate
```

### 7. Create a Superuser

To access Django's Admin Interface and manage the data, create a superuser:

```bash
python manage.py createsuperuser
```

This will help you access and manage the database using Django's admin interface.

## API Documentation

The project uses **drf-yasg** to generate Swagger documentation for the API. Once the project is running, you can access the API documentation at:

- **Swagger UI**: [https://wazitrack-backend.onrender.com/swagger/](https://wazitrack-backend.onrender.com/swagger/)

## API Endpoints

### **Authentication**

- **Register Farmer**: `POST /register/farmer`
- **Register Company**: `POST /register/company`
- **Sign In**: `POST /api/signin`

### **OTP Verification**

- **Request OTP**: `POST /otp/request`
- **Verify OTP**: `POST /otp/verify`
- **Resend OTP**: `POST /otp/resend`

## Running the Project

To run the project locally, use the following command:

```bash
python manage.py runserver
```

The application will be accessible at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

