##### Verbindung zur Datenbank herstellen #####

import mariadb

# Connect to the MySQL database
try:
    db = mariadb.connect(
        user="hems-lf8-03",
        password="Stp563FqwyZ0",
        database="LF08_DB"
    )
    print("Verbindung zur Datenbank erfolgreich hergestellt.")
except mariadb.Error as e:
    print(f"Fehler bei der Verbindung zur Datenbank: {e}")

# Die Methode prüft ob eine erfolgreiche Verbindung zur Datenbank hergestellt werden kann.
# Ausgabe: gibt "successful" oder "fail" als print-Ausgabe zurück
def testConnection(dbc):  # dbc steht für die Datenbankverbindung die überprüft werden soll
    try:
        cursor = dbc.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        print("successful")
    except mariadb.Error as e:
        print(f"fail: {e}")

# Aufruf der Methode zum Testen der Datenbankverbindung
testConnection(db)
