import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mariadb, csv, os
from db.db_connector import DbConnector

# definiere hier die SQl-Anweisung
sql_Anweisung= "SELECT * FROM artikel"
sql_Anweisung2 = "SELECT * FROM personal"
csv_file_path = "./csv/"


# gibt nach erfolgreicher Verbindung mit der Datenbank, die Sql-Abfrage zurück
def export_to_csv(dbc, table):
    try:
        sql = f"SELECT * FROM {table}"
        result = list()
        column_names = list()

        dbc.execute(sql) #execute sql-query and get result
        rows = dbc.fetchall()

        for columns in dbc.description: #get column names
            column_names.append(columns[0])
        result.append(column_names)
        
        for row in rows: #get row contents
            result.append(row)

        os.makedirs(os.path.dirname(csv_file_path), exist_ok=True) #create directory for csv files
        
        with open(csv_file_path + f"{table}" + ".csv", 'w', newline='') as csvfile: #write the csv file
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in result:
                csvwriter.writerow(row)

    except mariadb.Error as e:
        print(f"fail: {e}")
        return False