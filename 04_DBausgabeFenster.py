
import tkinter as tk
from tkinter import ttk
import mariadb
from db.db_connector import DbConnector

#Daten auslesen 
def read_from_database():
    db = DbConnector().db_connect()
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM personal")  
        db_rows = cursor.fetchall()

        rows = list()
        column_names = list()

        for columns in cursor.description:
            column_names.append(columns[0])

        rows.append(column_names)
        for db_row  in db_rows:
            rows.append(db_row)

        return column_names, db_rows
    except mariadb.Error as e:
        print(f"fail: {e}")
    finally:
        db.close()


# Tkinter-Setup
    
def darstellung_tabelle():








darstellung_tabelle()
