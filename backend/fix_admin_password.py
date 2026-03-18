from flask_bcrypt import Bcrypt
from db import get_db_connection

# Create a bcrypt instance (same as in app.py)
bcrypt = Bcrypt()

# Get database connection
db = get_db_connection()
cur = db.cursor()

# Hash the password
hashed = bcrypt.generate_password_hash("admin123").decode('utf-8')

# Update the admin user's password
cur.execute("""
    UPDATE tbl_user
    SET password_hash = %s
    WHERE Email = %s
""", (hashed, "admin@gmail.com"))

db.commit()
db.close()

print("Admin password updated successfully.")