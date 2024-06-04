
import tkinter as tk
from tkinter import ttk
import mariadb
from db.db_connector import DbConnector

#Daten auslesen 
def read_from_database(table):
    db = DbConnector().db_connect()
    try:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM {table}")  
        db_rows = cursor.fetchall()

        rows = list()
        column_names = list()

        for columns in cursor.description:
            column_names.append(columns[0])

        for db_row  in db_rows:
            rows.append(db_row)

        return column_names, db_rows
    except mariadb.Error as e:
        print(f"fail: {e}")
        return False
    finally:
        db.close()


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


# usae example
table = input("What table do you want to see? ")
result = read_from_database(table)
while result == False:
    table = input("Please try again: ")
    result = read_from_database(table)


darstellung_tabelle(columns=result[0], rows=result[1])
