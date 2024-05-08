import csv
import sqlite3 # Importerer modulene som jeg trenger for å få importert dataen fra csv filen til en database på riktig måte

# Kobler til databasen, eller lager den hvis den ikke eksisterer
conn = sqlite3.connect('SQL 2/test2.db')
cursor = conn.cursor()

# Lager tabellen med kolonner til dataen hvis en tabell med samme navn ikke eksisterer
cursor.execute('''CREATE TABLE IF NOT EXISTS PostInf ( 
    Postnummer varchar(255),
    Poststed TEXT,
    Kommunenummer TEXT,
    Kommunenavn TEXT,
    Kategori TEXT 
)''')

# Åpner CSV filen og leser innholdet
with open('SQL 2/Postnummerregister-Excel.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    data = [row for row in reader]

# Setter inn dataen i tabellen
    for row in data:
        cursor.execute("INSERT INTO PostInf (Postnummer, Poststed, Kommunenummer, Kommunenavn, Kategori)  VALUES (?, ?, ?, ?, ?)", row)

# Fullfører endringene og lukker tilkoblingen
conn.commit()
conn.close()
