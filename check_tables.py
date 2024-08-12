# from config import app, db
# from models import PreShipmentTask

# with app.app_context():
#     # Create all tables
#     db.create_all()
#     print("Tables created successfully.")


# import sqlite3

# # Connect to the SQLite database
# conn = sqlite3.connect('database.db')
# cursor = conn.cursor()

# # List all tables
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cursor.fetchall()

# print("Tables in database:", tables)

# # Check if the specific table exists
# if ('pre_shipment_task',) in tables:
#     print("Table 'pre_shipment_task' exists.")
#     cursor.execute("PRAGMA table_info(pre_shipment_task);")
#     columns = cursor.fetchall()
#     print("Columns in 'pre_shipment_task':")
#     for column in columns:
#         print(column)
# else:
#     print("Table 'pre_shipment_task' does not exist.")

# # Close the connection
# conn.close()


# from app import db  # Import db from your Flask app

# # Reflect the database schema
# db.reflect()

# # Print the table names
# print("Tables in database:", db.engine.table_names())



from your_flask_app import db
from models import PreShipmentTask  # Import your model

# Create all tables in the database
db.create_all()

# Reflect the database schema
db.reflect()

# Print the table names
print("Tables in database:", db.engine.table_names())



