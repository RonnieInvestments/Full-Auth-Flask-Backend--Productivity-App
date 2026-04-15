## Productivity App Backend (Flask + JWT Auth)
## Project Description

This project is a backend API for a productivity/journal application built using Flask. It provides secure user authentication and allows users to create and manage journal entries.

The system implements JWT-based authentication, database persistence using SQLAlchemy, and schema validation with Marshmallow. It demonstrates real-world backend architecture, including authentication, relationships, and database migrations.

## System Architecture

## Explanation:

Clients interact with the Flask API via HTTP requests
JWT handles authentication and access control*
SQLAlchemy manages database operations
Flask-Migrate handles schema evolution

## Features
User registration and authentication (JWT)*
Secure password handling (bcrypt)
CRUD operations for journal entries
Pagination support for large datasets
Database integration with SQLAlchemy
Schema validation using Marshmallow
Database migrations using Flask-Migrate

## Tech Stack
Backend Framework: Flask
Database: SQLite
ORM: SQLAlchemy
Authentication: JWT (Flask-JWT-Extended)*
Password Hashing: Flask-Bcrypt
Migrations: Flask-Migrate
Validation: Marshmallow

## Installation and Setup Instructions

## 1. Clone the Repository

git clone <your-repo-url>
cd Full-Auth-Flask-Backend--Productivity-App

## 2. Create and Activate Virtual Environment

python3 -m venv venv
source venv/bin/activate

## 3. Install Dependencies
pip install -r requirements.txt

## Running the Application
Start the Flask Server
flask run

## Default base URL:

http://127.0.0.1:5000


## Database Setup
Initialize Migrations
flask db init
Generate Migration
flask db migrate -m "Initial migration"
Apply Migration
flask db upgrade

## Seed Database
python seed.py


## API Endpoint Overview
## Authentication
Register User
POST /register
{
  "username": "testuser",
  "password": "password123"
}
Login User
POST /login

Returns JWT token.

## Journal Entries

## Get All Entries (Paginated)
GET /entries?page=1
Create Entry
POST /entries
{
  "title": "My Day",
  "content": "Today I learned Flask."
}

Requires JWT token*

## Update Entry
PATCH /entries/<id>

## Delete Entry
DELETE /entries/<id>

## Request Flow Example


## Project Structure
server/
├── app.py          # Main Flask application
├── models.py       # Database models & schemas
├── seed.py         # Seed data script
├── migrations/     # Database migrations


## Code Quality and Design
Clear separation of concerns (routes, models, config)
Use of ORM for database abstraction
JWT-based stateless authentication*
Input validation with Marshmallow
Scalable structure for future expansion


## Future Improvements
Add role-based authorization (admin/user)
Implement refresh tokens
Add unit and integration testing (pytest)
Deploy using Docker
Integrate a frontend (React or Vue)
Add search and filtering for entries

## Author

Backend API project demonstrating:
Authentication and authorization
RESTful API design
Database modeling and migrations
Scalable Flask application architecture