import sqlite3

# Connect to the database
conn = sqlite3.connect('logisticsdatabase.db')
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM pre_shipment_task")

# Fetch all results
rows = cursor.fetchall()

# Print each row
for row in rows:
    print(row)
    

# Close the connection
conn.close()
