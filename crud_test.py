from database import SessionLocal
from models.user import User

db = SessionLocal()

new_user = User(
    email="test@example.com",
    password_hash="hashedpassword123",
    name="Test User"
)

existing_user = db.query(User).filter(User.email == "test@example.com").first()

if not existing_user:
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print("New user id: ", new_user.id)

else:
    print("User already exists with ID: ", existing_user.id)

users = db.query(User).all()

for user in users:
    print(user.id, user.name, user.email)