# CRUD Operation with FastAPI and MySQL

A FastAPI application for performing CRUD (Create, Read, Update, Delete) operations on a MySQL database using SQLAlchemy.

## Features

- **Create**: Add new records to the database.
- **Read**: Retrieve records from the database.
- **Update**: Modify existing records.
- **Delete**: Remove records from the database.

## Prerequisites

- Python 3.7+
- MySQL database

## Project Structure

main.py:  Contains the FastAPI app with routes 

db.py:  Database configuration and connection 

model.py:  SQLAlchemy model for User

README.md:  Project documentation


## Database Configuration

Edit `database.py` to include your MySQL connection details:

```python
URL = "mysql+pymysql://<username>:<password>@localhost/<database_name>"
```
Replace username, password, and database_name with your MySQL credentials.

### Running the Application

Start the FastAPI server:
```
uvicorn main:app --reload
```

Access the API documentation at:

OpenAPI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc


### API Endpoints

POST /add/: Add a new user

GET /alluser/: Retrieve all users

GET /user/id/{user_id}: Get a user by ID

PUT /user/update/{user_id}: Update user details (to be added)

DELETE /user/delete/{user_id}: Delete a user (to be added)
