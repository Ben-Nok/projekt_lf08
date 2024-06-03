import mariadb, csv, os
from db.db_connector import DbConnector

# Connect to the MySQL database 
# - definiere hier die Verbindung zur Datenbank
cursor=DbConnector().db_connect().cursor()

# definiere hier die SQl-Anweisung
sql_Anweisung= "SELECT * FROM artikel"
sql_Anweisung2 = "SELECT * FROM personal"
csv_file_path = "./csv/artikel.csv"


# gibt nach erfolgreicher Verbindung mit der Datenbank, die Sql-Abfrage zurück
def testprint(sql):
    try:
        result = list()
        column_names = list()

        cursor.execute(sql) #execute sql-query and get result
        rows = cursor.fetchall()

        for columns in cursor.description: #get column names
            column_names.append(columns[0])
        result.append(column_names)
        
        for row in rows: #get row contents
            result.append(row)

        os.makedirs(os.path.dirname(csv_file_path), exist_ok=True) #create directory for csv files
        
        with open(csv_file_path, 'w', newline='') as csvfile: #write the csv file
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in result:
                csvwriter.writerow(row)

    except mariadb.Error as e:
        print(f"fail: {e}")
    finally:
        cursor.close()


testprint(sql_Anweisung)
testprint(sql_Anweisung2)