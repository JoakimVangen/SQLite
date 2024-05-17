import sqlite3
import csv
# Importerer modulene jeg trenger for å lese CSV-filer og jobbe med SQLite-databaser


# Lager og kobler til databasen
conn = sqlite3.connect('kundeliste.db')
cursor = conn.cursor()

# Lager tabellene
cursor.execute('''
CREATE TABLE IF NOT EXISTS postnummer (
    postnummer INT,
    poststed TEXT NOT NULL,
    kommunenummer INTEGER NOT NULL,
    kommunenavn TEXT NOT NULL
)
''') # Lager tabellen for postnummer

cursor.execute('''
CREATE TABLE IF NOT EXISTS kundeliste (
    kundenummer INT,
    fornavn TEXT NOT NULL,
    etternavn TEXT NOT NULL,
    epost TEXT NOT NULL,
    telefon TEXT NOT NULL,
    postnummer INTEGER NOT NULL,
    FOREIGN KEY (postnummer) REFERENCES postnummer_tabell(postnummer)
)
''') # Lager tabellen for kundeliste

# Funksjon for å lese CSV-fil og fylle tabellen
def funcles_csv_og_fyll_tabell(filnavn, tabellnavn, kolonner):
    with open(filnavn, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        print("Kolonnenavn i CSV-filen:", reader.fieldnames)
        for row in reader:
            try:
                verdier = tuple(row[kolonne] for kolonne in kolonner)
                sporsmalstegn = ','.join('?' * len(kolonner))
                cursor.execute(f'INSERT INTO {tabellnavn} ({",".join(kolonner)}) VALUES ({sporsmalstegn})', verdier)
            except KeyError as e:
                print(f"NøkkelError: {e}. Sjekk at kolonnenavnene i CSV-filen matcher de forventede navnene.")

# Fylle tabellene med data fra CSV-filene
funcles_csv_og_fyll_tabell('SQL 3/Postnummer.csv', 'postnummer_tabell', ['postnummer', 'poststed', 'kommunenummer', 'kommunenavn'])
funcles_csv_og_fyll_tabell('SQL 3/Kundeliste2.csv', 'kundeinfo', ['kundenummer', 'fornavn', 'etternavn', 'epost', 'telefon', 'postnummer'])

# Funksjon for å hente og vise kundedetaljer
def funcvis_kundeinfo(kundenummer):
    query = '''
    SELECT 
        k.kundenummer, k.fornavn, k.etternavn, k.epost, k.telefon, 
        p.postnummer, p.poststed, p.kommunenummer, p.kommunenavn
    FROM 
        kundeinfo k
    JOIN 
        postnummer_tabell p ON k.postnummer = p.postnummer
    WHERE 
        k.kundenummer = ?
    '''
    cursor.execute(query, (kundenummer,))
    result = cursor.fetchone()
    
    if result:
        print(f"Kundenummer: {result[0]}")
        print(f"Fornavn: {result[1]}")
        print(f"Etternavn: {result[2]}")
        print(f"E-post: {result[3]}")
        print(f"Telefon: {result[4]}")
        print(f"Postnummer: {result[5]}")
        print(f"Poststed: {result[6]}")
        print(f"Kommunenummer: {result[7]}")
        print(f"Kommunenavn: {result[8]}")
    else:
        print("Ingen kunde funnet med dette kundenummeret.")

# Hovedprogram
if __name__ == '__main__':
    kundenummer = input("Vennligst skriv inn kundenummer: ")
    funcvis_kundeinfo(int(kundenummer))

# Lukke databasen
conn.commit()
conn.close()
