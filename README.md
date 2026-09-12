# Sample_program-API

Author: Saurabh Raj

## Overview

This project is a simple API built with [FastAPI](https://fastapi.tiangolo.com/).
It currently provides basic home, about, and users routes.

## Requirements

- Python 3.8 or newer
- FastAPI
- Uvicorn

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install fastapi uvicorn
```

## Running the API

Start the development server from the project directory:

```bash
uvicorn create_route:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Routes

### Home

```http
GET /
```

Response:

```json
{
	"message": "create the home route"
}
```

### About

```http
GET /About
```

Response:

```json
{
	"message": "This is about page"
}
```

### Users

```http
GET /Users
```

Response:

```json
{
	"users": [
		"Saurabh",
		"Nayra",
		"Shubham",
		"Mohit"
	]
}
```

## Interactive Documentation

FastAPI automatically generates interactive API documentation:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Project Structure

```text
Sample_program-API/
├── create_route.py   # FastAPI application and route definitions
└── README.md         # Project documentation
```

## Git Branch

The current development branch is:

```text
feature/crud-operation
```

This branch can be used to add create, read, update, and delete operations in the future.
