import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("school.db")
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS Students (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Age INTEGER,
    Grade TEXT
)
""")

# Insert data
data = [
    ("Alice", 20, "A"),
    ("Bob", 21, "B")
]

cur.executemany(
    "INSERT INTO Students (Name, Age, Grade) VALUES (?, ?, ?)",
    data
)

conn.commit()

# Display records
print("Students:")
for row in cur.execute("SELECT * FROM Students"):
    print(row)

# Delete record
cur.execute("DELETE FROM Students WHERE ID = 1")
conn.commit()

# Display after deletion
print("\nAfter Deletion:")
for row in cur.execute("SELECT * FROM Students"):
    print(row)

# Close connection
conn.close()
