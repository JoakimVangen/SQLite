import csv
import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Create a table to store the data
cursor.execute('''CREATE TABLE IF NOT EXISTS Brukere (
    fname varchar(255),
    ename TEXT,
    epost TEXT,
    tlf TEXT,
    postnummer TEXT 
)''')

# Open the CSV file and read its contents
with open('randoms.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    data = [row for row in reader]

# Insert the data into the table
    for row in data:
        cursor.execute("INSERT INTO Brukere (fname, ename, epost, tlf, postnummer)  VALUES (?, ?, ?, ?, ?)", row)

# Commit the changes and close the connection
conn.commit()
conn.close()