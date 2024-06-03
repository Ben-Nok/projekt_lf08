import mariadb, csv, os
from db.db_connector import DbConnector

# Connect to the MySQL database 
# - definiere hier die Verbindung zur Datenbank
db=DbConnector().db_connect()
cursor = db.cursor()

# definiere hier die SQl-Anweisung
sql_Anweisung= "SELECT * FROM artikel"
csv_file_path = "./csv/artikel.csv"


# gibt nach erfolgreicher Verbindung mit der Datenbank, die Sql-Abfrage zurück
def testprint(sql):
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()

        result = list()
        column_names = list()

        for columns in cursor.description:
            column_names.append(columns[0])

        result.append(column_names)
        for row in rows:
            result.append(row)

        os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)
        
        with open(csv_file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in result:
                csvwriter.writerow(row)

    except mariadb.Error as e:
        print(f"fail: {e}")
    finally:
        db.close()


testprint(sql_Anweisung)