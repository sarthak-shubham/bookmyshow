from sqlalchemy.orm import Session
from auth.hashing import hash_password, verify_password
from models.user import User
from auth.jwt_handler import create_access_token


def create_user(db: Session, email: str, password: str, name: str):

    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise ValueError("Email already registered")
    
    hashed_password = hash_password(password)

    new_user = User(
        email = email,
        password_hash = hashed_password,
        name = name
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def authenticate_user(db: Session, email: str, password: str):

    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    
    if not verify_password(password, user.password_hash):
        return None
    
    return user


def login_user(db: Session, email: str, password: str):

    user = authenticate_user(db, email, password)
    if not user:
        return None
    
    access_token = create_access_token({"user_id": user.id})

    return access_token