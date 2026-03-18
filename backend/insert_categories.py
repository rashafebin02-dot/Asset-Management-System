import mysql.connector
from db import get_db_connection

# Sample categories for asset management
categories = [
    {
        "name": "Computers",
        "description": "Desktop computers, laptops, and workstations"
    },
    {
        "name": "Monitors",
        "description": "Display monitors and screens"
    },
    {
        "name": "Printers",
        "description": "Printers, scanners, and multifunction devices"
    },
    {
        "name": "Network Equipment",
        "description": "Routers, switches, and networking devices"
    },
    {
        "name": "Office Furniture",
        "description": "Desks, chairs, cabinets, and other furniture"
    },
    {
        "name": "Software Licenses",
        "description": "Software licenses and subscriptions"
    },
    {
        "name": "Mobile Devices",
        "description": "Phones, tablets, and mobile devices"
    },
    {
        "name": "Peripherals",
        "description": "Keyboards, mice, headphones, and other peripherals"
    },
    {
        "name": "Server Equipment",
        "description": "Servers and server-related equipment"
    },
    {
        "name": "Storage Devices",
        "description": "Hard drives, SSDs, USB drives, and storage media"
    }
]

try:
    db = get_db_connection()
    cursor = db.cursor()
    
    for category in categories:
        try:
            cursor.execute("""
                INSERT INTO tbl_category (Category_name, Category_description)
                VALUES (%s, %s)
            """, (category["name"], category["description"]))
            
            print(f"✓ Inserted: {category['name']}")
        except mysql.connector.Error as err:
            if err.errno == 1062:  # Duplicate entry
                print(f"⚠ Skipped: {category['name']} (already exists)")
            else:
                print(f"✗ Error inserting {category['name']}: {err}")
    
    db.commit()
    print("\n✓ All categories inserted successfully!")
    
except Exception as e:
    print(f"Connection error: {e}")
finally:
    if db:
        db.close()
