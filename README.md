# FastAPI Tea API

A simple CRUD-based REST API project developed using FastAPI and Pydantic for learning backend API development and request handling.

---

## Overview

This project demonstrates the implementation of RESTful API operations using Python and FastAPI. The API allows users to perform Create, Read, Update, and Delete (CRUD) operations on tea items. The project was created to practice backend development concepts such as API routing, request validation, JSON handling, and server-side logic.

Instead of using a database, Python lists were used as temporary in-memory storage for testing and understanding API workflows.

---

## Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn
* Virtual Environment (venv)

---

## Features

* Create tea items using POST requests
* Retrieve all tea items using GET requests
* Update tea records using PUT requests
* Delete tea records using DELETE requests
* Automatic API documentation with Swagger UI
* Request validation using Pydantic models
* Lightweight in-memory data storage using Python lists

---

## Project Structure

```bash
project-folder/
│
├── venv/
├── __pycache__/
├── main.py
└── requirements.txt
```

---

## API Endpoints

### Home Route

```http
GET /
```

Returns welcome message.

---

### Get All Teas

```http
GET /teas
```

Returns all tea records.

---

### Add Tea

```http
POST /teas/
```

Example Request Body:

```json
{
  "id": 1,
  "name": "Green Tea",
  "origin": "India"
}
```

---

### Update Tea

```http
PUT /teas/{tea_id}
```

Updates an existing tea record.

---

### Delete Tea

```http
DELETE /teas/{tea_id}
```

Deletes a tea record.

---

## How to Run the Project

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

#### PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

#### CMD

```cmd
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run FastAPI Server

```bash
uvicorn main:app --reload
```

---

## Swagger API Documentation

After running the server, open:

```text
http://127.0.0.1:8000/docs
```

FastAPI automatically generates interactive API documentation for testing endpoints.

---

## Learning Outcomes

Through this project, the following concepts were practiced:

* REST API development
* FastAPI routing
* CRUD operations
* Pydantic data validation
* JSON request/response handling
* Python backend development
* API testing with Swagger UI
* Virtual environment management
* Dependency management using requirements.txt

---

## Future Improvements

Possible future upgrades for this project:

* MongoDB or PostgreSQL integration
* User authentication with JWT
* Database ORM integration
* Docker deployment
* Frontend integration using React
* Cloud deployment

---

## Author

Develo
