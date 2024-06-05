import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

##### Verbindung zur Datenbank herstellen #####

import mariadb
from db.db_connector import DbConnector

# Connect to the MySQL database
try:
    db = DbConnector().db_connect()
    print("Verbindung zur Datenbank erfolgreich hergestellt.")
except mariadb.Error as e:
    print(f"Fehler bei der Verbindung zur Datenbank: {e}")

# Die Methode prüft ob eine erfolgreiche Verbindung zur Datenbank hergestellt werden kann.
# Ausgabe: gibt "successful" oder "fail" als print-Ausgabe zurück
def testConnection():  # dbc steht für die Datenbankverbindung die überprüft werden soll
    try:
        cursor = db.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        print("successful")
    except mariadb.Error as e:
        print(f"fail: {e}")

# 1.2 Methode um alle Mitarbeiter aus der Datenbank auszugeben
def printAllEmployees():
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM personal")  
        rows = cursor.fetchall()
        
        if rows:
            for row in rows:
                print(row)
                cursor.close()
        else:
            print("Keine Mitarbeiter gefunden.")
            cursor.close()
        
        cursor.close()
    except mariadb.Error as e:
        print(f"Fehler beim Abrufen der Mitarbeiter: {e}")

# Aufruf der Methode zum Testen der Datenbankverbindung
testConnection()

# Aufruf der Methode um alle Mitarbeiter auszugeben
printAllEmployees()