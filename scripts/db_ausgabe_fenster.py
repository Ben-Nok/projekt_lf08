import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import ttk
import mariadb
from db.db_connector import DbConnector

#Daten auslesen 
def read_from_database(dbc, table):
    try:
        cursor = dbc.cursor()
        cursor.execute(f"SELECT * FROM {table}")  
        db_rows = cursor.fetchall()

        rows = list()
        column_names = list()

        for columns in cursor.description:
            column_names.append(columns[0])

        for db_row  in db_rows:
            rows.append(db_row)

        darstellung_tabelle(column_names, db_rows)
    except mariadb.Error as e:
        print(f"fail: {e}")
        return False
    finally:
        dbc.close()


# Tkinter-Setup
def darstellung_tabelle(columns, rows):
    root = tk.Tk()
    root.title("Datenbank Tabelle")

    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create the Treeview widget
    tree = ttk.Treeview(frame, columns=columns, show='headings', height=8)

    # Define the columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    # Insert the data into the table
    for row in rows:
        tree.insert('', 'end', values=row)

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Pack the treeview widget
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    root.mainloop()

