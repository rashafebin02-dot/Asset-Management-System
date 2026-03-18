import mysql.connector
from flask_bcrypt import Bcrypt
from db import get_db_connection

bcrypt = Bcrypt()

# Test users data
test_users = [
    {
        "username": "admin",
        "email": "admin@gmail.com",
        "password": "admin123",
        "user_type": "Admin",
        "phone": "9999999999"
    },
    {
        "username": "manager1",
        "email": "manager@gmail.com",
        "password": "manager123",
        "user_type": "Manager",
        "phone": "8888888888"
    },
    {
        "username": "user1",
        "email": "user@gmail.com",
        "password": "user123",
        "user_type": "User",
        "phone": "7777777777"
    },
    {
        "username": "staff1",
        "email": "staff@gmail.com",
        "password": "staff123",
        "user_type": "Staff",
        "phone": "6666666666"
    },
    {
        "username": "auditor1",
        "email": "auditor@gmail.com",
        "password": "auditor123",
        "user_type": "Auditor",
        "phone": "5555555555"
    }
]

try:
    db = get_db_connection()
    cursor = db.cursor()
    
    # Clear existing users (optional - comment out if you want to keep existing)
    # cursor.execute("DELETE FROM tbl_user")
    
    for user in test_users:
        # Hash the password
        hashed_password = bcrypt.generate_password_hash(user["password"]).decode('utf-8')
        
        try:
            cursor.execute("""
                INSERT INTO tbl_user (User_name, Email, password_hash, user_type, Phone_no)
                VALUES (%s, %s, %s, %s, %s)
            """, (user["username"], user["email"], hashed_password, user["user_type"], user["phone"]))
            
            print(f"✓ Inserted: {user['username']} ({user['user_type']}) - Password: {user['password']}")
        except mysql.connector.Error as err:
            if err.errno == 1062:  # Duplicate entry
                print(f"⚠ Skipped: {user['email']} (already exists)")
            else:
                print(f"✗ Error inserting {user['username']}: {err}")
    
    db.commit()
    print("\n✓ All test users inserted successfully!")
    
except Exception as e:
    print(f"Connection error: {e}")
finally:
    if db:
        db.close()
