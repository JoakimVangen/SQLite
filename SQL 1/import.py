import csv
import sqlite3 # Importerer modulene som jeg trenger for å få importert dataen fra csv filen til en database riktig

# Kobler til databasen, eller lager den hvis den ikke eksisterer
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Lager tabellen med kolonner til dataen, hvis en tabell med samme navn ikke eksisterer
cursor.execute('''CREATE TABLE IF NOT EXISTS Brukere (
    fname varchar(255),
    ename TEXT,
    epost TEXT,
    tlf TEXT,
    postnummer TEXT 
)''')

# Åpner CSV filen og leser innholdet
with open('randoms.csv', 'r') as f:
    reader = csv.reader(f) 
    next(reader)  # Skip the header row
    data = [row for row in reader] # Leser inn dataen fra csv filen

# Setter inn dataen i tabellen
    for row in data:
        cursor.execute("INSERT INTO Brukere (fname, ename, epost, tlf, postnummer)  VALUES (?, ?, ?, ?, ?)", row)

# Fullfører endringene og lukker tilkoblingen
conn.commit()
conn.close()