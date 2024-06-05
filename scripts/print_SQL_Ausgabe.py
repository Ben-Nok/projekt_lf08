import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mariadb
from db.db_connector import DbConnector

# gibt nach erfolgreicher Verbindung mit der Datenbank, die Sql-Abfrage zurück
def testprint(dbc: mariadb.Connection, table: str):
    try:
        cursor = dbc.cursor()
        cursor.execute(f"SELECT * FROM {table}")  
        rows = cursor.fetchall()
        
        if rows:
            for row in rows:
                print(row)
                cursor.close()
        else:
            print("No Entries found.")
            cursor.close()
        
    except mariadb.Error as e:
        print(f"fail: {e}")
        return False