# Full-Auth-Flask-Backend--Productivity-App
Overview

This project is a backend API for a productivity and journal management application built using Flask. It provides a complete authentication system and supports CRUD operations for journal entries, allowing users to create, read, update, and manage their personal productivity logs.

The application is designed with scalability and maintainability in mind, incorporating pagination, structured schemas, and database migrations.

Features
User authentication using JWT (JSON Web Tokens)*
Secure password hashing
Create, read, and update journal entries
Pagination support for efficient data retrieval
RESTful API design
Database migrations with Flask-Migrate
Input validation and serialization using schemas

Tech Stack
Python 3
Flask
Flask SQLAlchemy
Flask Migrate
Flask JWT Extended*
Marshmallow (for serialization and validation)
SQLite (default database)
Bcrypt (for password hashing)


Project Structure
productivity_app/
│
├── server/
│   ├── app.py              # Main application entry point
│   ├── models.py           # Database models
│   ├── schemas.py          # Serialization and validation schemas
│   └── config.py           # Configuration settings (if present)
│
├── migrations/             # Database migration files
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation

Installation and Setup

1. Clone the Repository

git clone <your-repo-url>
cd productivity_app

2. Create a Virtual Environment

python -m venv venv

Activate the environment:

Windows:

venv\Scripts\activate

macOS/Linux:

source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Set Up the Database

Initialize migrations:

flask db init

Create migration:

flask db migrate -m "Initial migration"

Apply migration:

flask db upgrade

5. Run the Application

flask run

The server will start on:

http://127.0.0.1:5000
API Endpoints
Base Route
GET /

Response:

{
  "message": "Welcome to our journal entry platform"
}
Get All Journal Entries (Paginated)
GET /entries?page=1&per_page=5

Response:

{
  "page": 1,
  "per_page": 5,
  "total": 20,
  "total_pages": 4,
  "items": [ ... ]
}
Create Journal Entries
POST /entries

Request Body:

[
  {
    "title": "My Day",
    "content": "Today was productive..."
  }
]

Response:

201 Created
Update Journal Entry
PATCH /entry/<id>

Request Body:

{
  "title": "Updated Title",
  "content": "Updated content"
}
Authentication


Login

Users receive an access token after successful authentication, which must be included in protected routes:

Authorization: Bearer <your_token>
Database
Default: SQLite (entries.db)
ORM: SQLAlchemy
Migrations handled via Flask-Migrate
Error Handling

The API includes basic error handling for:

Invalid input data
Validation errors
Database operation failures

Example:

{
  "message": "Could not load the data"
}
Future Improvements
Add DELETE endpoint for entries
Implement role-based access control
Add frontend (React.js)
Improve error messaging and logging
Add unit and integration tests
Dockerize the application


Author

Developed as part of a final project for backend development using Flask.

License

This project is for educational purposes. 
Please modify and reuse it as needed.