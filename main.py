# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
from models import User, Base

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for request body
class UserCreate(BaseModel):
    name: str

# Pydantic model for response
class UserRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True    


@app.get('/')
def hello():
    return "Home Page"

# POST request to insert a new user
@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=user.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    # return {"message": f"User {new_user.name} with ID {new_user.id} created successfully"}
    return f"{new_user.name} is created with id {new_user.id}"

# GET request to retrieve all users
@app.get("/users/", response_model=list[UserRead])
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


# PUT request to update an existing user by ID
@app.put("/users/{user_id}", response_model=dict)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update the user's name
    existing_user.name = user.name
    db.commit()
    db.refresh(existing_user)
    
    return {"message": f"User with ID {user_id} updated successfully"}

# DELETE request to remove a user by ID
@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Delete the user from the database
    db.delete(existing_user)
    db.commit()
    
    return {"message": f"User with ID {user_id} deleted successfully"}