from database import SessionLocal
from models.user import User

db = SessionLocal()

try:
    user = User(
        email="rollback@test.com",
        password_hash="hash123",
        name="Rollback User"
        )
    
    db.add(user)

    raise Exception("Simulated failure before commit")

except Exception as e:
    print("Error occured:", e)
    db.rollback()

finally:
    db.close()