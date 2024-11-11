 Project Name: **Flask Authentication API**

## Overview
This project is a simple Flask-based API that provides user authentication and registration functionalities. It supports JWT-based authentication, user registration, and login with password hashing and verification.

## Features
- **User Registration**: Register new users with hashed passwords.
- **User Login**: Login users and generate a JWT token for authentication.
- **JWT Authentication**: Secure API access using JWT (JSON Web Tokens).
- **Database Integration**: Uses SQLAlchemy with MySQL (or SQLite) for persistent storage.
- **Error Handling**: Proper validation and error responses for registration and login requests.

## Technologies Used
- **Backend**: Flask
- **Database**: MySQL / SQLite
- **Authentication**: JWT (Flask-JWT-Extended)
- **ORM**: SQLAlchemy
- **Environment Variables**: Dotenv
- **Password Hashing**: Bcrypt (for secure password storage)

## Setup & Installation

### 1. Clone the repository:
```bash
git clone https://github.com/Jhaveri-Jeet/Flask-API.git
cd Flask-API
```

### 2. Create and activate the virtual environment:
Run the following command to create the virtual environment:
```bash
python3 -m venv path/to/your/virtualenv
```
Activate the virtual environment:
- On Windows:
  ```bash
  path\to\your\virtualenv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source path/to/your/virtualenv/bin/activate
  ```

### 3. Install dependencies:
Once the virtual environment is activated, install the required packages by running:
```bash
pip install -r requirements.txt
```

### 4. Start XAMPP and Set Up the Database:
- Make sure your **XAMPP server** is running. You will need to start **Apache** and **MySQL** from the XAMPP control panel.
- Open **phpMyAdmin** (usually accessible via `http://localhost/phpmyadmin/`).
- Create a new database, for example `flask_auth_db`.
- Update your `.env` file with the correct database connection information:
  ```env
  SECRET_KEY=your_secret_key
  SQLALCHEMY_DATABASE_URI=mysql+pymysql://username:password@localhost/flask_auth_db
  SQLALCHEMY_TRACK_MODIFICATIONS=False
  JWT_SECRET_KEY=your_jwt_secret_key
  ```

### 5. Create the database:
Run the following commands to create the necessary database tables:
```bash
python
>>> from app import db
>>> db.create_all()
```

### 6. Run the application:
Start the Flask application using:
```bash
flask run
```
By default, it will be accessible at `http://localhost:5000`.

## API Endpoints

### 1. **User Registration**
- **Endpoint**: `/user/register`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "password": "securePassword"
  }
  ```
- **Response**:
  - `201 Created`: User successfully created.
  - `400 Bad Request`: Missing fields or invalid data.
  - `409 Conflict`: Email already exists.

### 2. **User Login**
- **Endpoint**: `/user/login`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "johndoe@example.com",
    "password": "securePassword"
  }
  ```
- **Response**:
  - `200 OK`: Successfully logged in, returns JWT token.
  - `401 Unauthorized`: Invalid credentials.

### 3. **Protected Endpoint (Requires JWT)**
- **Endpoint**: `/user/profile`
- **Method**: `GET`
- **Authentication**: Bearer JWT token in the header.
- **Response**: User profile details if the token is valid.


## Database Schema
### `User` Model:
- `id`: Integer (Primary Key)
- `name`: String
- `email`: String (Unique)
- `password_hash`: String (Hashed password)
