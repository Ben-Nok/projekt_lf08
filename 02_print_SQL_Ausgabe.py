import mariadb
from db.db_connector import DbConnector

# Connect to the MySQL database 
# - definiere hier die Verbindung zur Datenbank
# Connect to the MySQL database
try:
    db = DbConnector().db_connect()
except mariadb.Error as e:
    print(f"Error while trying to connect: {e}")


# gibt nach erfolgreicher Verbindung mit der Datenbank, die Sql-Abfrage zurück
def testprint(query):
    try:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM {query}")  
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


# definiere hier die SQl-Anweisung
query = input("Which database should be outputted? ")
result = testprint(query)
while result == False: #if read_from_database returns false ask for retry
    query = input("Please try again: ")
    result = testprint(query)