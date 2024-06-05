import tkinter as tk
import mariadb
from db.db_connector import DbConnector
from scripts.csv_to_xml import convert_csv_to_xml
from scripts.db_ausgabe_fenster import read_from_database
from scripts.db_in_CSV import export_to_csv
from scripts.print_SQL_Ausgabe import testprint
from scripts.xml_to_csv import convert_xml_to_csv
from tkinter import ttk, StringVar, Label, Button, Entry, OptionMenu #Grafik-Bib
import subprocess # Andere Pythonprgramme ausführen

mitarbeiter_options=["Lager", "Verwaltung", "Marketing", "Geschäftsführung"] # Nutzer Gruppenspezifisch für Login
login_successful = False

#initialize tk and set tk vars
root = tk.Tk()
root.geometry("300x200") #Adjust window size

#global tk variables
department_var = tk.StringVar()
passw_var = tk.StringVar()
status_var = tk.StringVar()
tool_var = tk.StringVar()
table_var = tk.StringVar()


def create_dropdown_login():
    root.geometry("300x300") #Adjust window size
    
    #Create Dropdown menu 
    drop_label = Label(root, text = "Abteilung: ", font = ('calibre',10,'bold'))
    department_var.set("Abteilung") #initial menu text
    dropdown = OptionMenu(root, department_var, *mitarbeiter_options) 

    #Create password input
    passw_label = Label(root, text = 'Password: ', font = ('calibre',10,'bold'), justify="center")
    passw_entry = Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*', width="15")

    #Create button, it will change label text 
    login_button = Button(root, text = "Login", command = submit)

    #login feedback
    status_label = Label(root, textvariable=status_var, font = ('calibre',10,'normal'), justify="left", wraplength=170)

    #create grid layout
    drop_label.grid(row=0, column=0, sticky="w")
    dropdown.grid(row=0, column=1, sticky="w")
    passw_label.grid(row=1, column=0, sticky="w")
    passw_entry.grid(row=1, column=1, sticky="w")
    login_button.grid(row=2, column=1, sticky="w")
    status_label.grid(row=3, column=1, sticky="w")

    root.bind('<Return>', lambda event: submit()) #bind submit to return key 


def submit():
    #submit password
    department = department_var.get()
    password = passw_var.get()
    global login_successful

    #check department option
    if(department not in mitarbeiter_options):
        status_var.set("Bitte wählen sie eine Abteilung!")
        login_successful = False
        return

    #validate password
    if(password == ""):
        status_var.set("Bitte geben sie ein Password ein!")
        login_successful = False
    elif(password != department):
        status_var.set("Falsches Passwort!")
        login_successful = False
    elif(password == department):
        status_var.set("Erfolgreich eingeloggt!")
        login_successful = True
    
    if(login_successful == True):
        show_accessable_tools() #draw tools, database, and execute ui-elements

    
def show_accessable_tools():
    tool_options = get_tool_options(department_var.get()) #get tool options

    #initialize tool select, label and button
    tool_var.set("Bitte wählen...")
    tool_label = Label(root, text = "Tools: ", font = ('calibre',10,'bold'))
    tool_dropdown = OptionMenu(root, tool_var, *tool_options)
    execute_button = Button(root, text = "Ausführen", command = execute_script) #button calls the execute_script() function
    
    #add elements to grid
    tool_label.grid(row=4, column=0, sticky="w")
    tool_dropdown.grid(row=4, column=1)
    show_select_table()#add select table dropdown
    execute_button.grid(row=6, column=1, sticky="w")


def show_select_table():
    table_options = get_all_tables()#get all tables as table options

    #initialize table select and label
    table_var.set("Bitte wählen...")
    table_label = Label(root, text = "Datenbank: ", font = ('calibre',10,'bold'))
    table_dropdown = OptionMenu(root, table_var, *table_options)
    
    #add elements to grid
    table_label.grid(row=5, column=0, sticky="w")
    table_dropdown.grid(row=5, column=1)


def get_all_tables():
    try:
        # Connect to the MySQL database
        dbc = DbConnector().db_connect()
        cursor = dbc.cursor()
        
        cursor.execute("SHOW TABLES")#get tables
        tables = cursor.fetchall()
        table_list = [table[0] for table in tables] #create table list and return lsit with table names
        return table_list
    except mariadb.Error as e:
        print(f"Fehler bei der Verbindung zur Datenbank: {e}")


def get_tool_options(department):
    #based on department parameter, different scripts will be returned as options
    if(department == "Lager"):
        return ["print_SQL_Ausgabe"]
    elif(department == "Verwaltung"):
        return ["print_SQL_Ausgabe", "DBinCSV", "DBausgabeFenster"]
    elif(department == "Marketing"):
        return ["print_SQL_Ausgabe", "DBausgabeFenster", "CSV_to_XML", "XML_to_CSV"]
    elif(department == "Geschäftsführung"):
        return ["print_SQL_Ausgabe", "DBinCSV", "DBausgabeFenster", "CSV_to_XML", "XML_to_CSV"]
    

def execute_script():
    try:
         #Connect to the MySQL database and create connection object
        dbc = DbConnector().db_connect()
    except mariadb.Error as e:
        print(f"Fehler bei der Verbindung zur Datenbank: {e}")
    
    #get selected values from the tool and table dropdown
    tool = tool_var.get()
    table = table_var.get()

    #execute the scripts with the connection object and the target table
    #the tools "XML_to_CSV" and "CSV_to_XML" dont need a table selection
    if(table != "Bitte wählen..." or tool == "XML_to_CSV" or tool == "CSV_to_XML"):
        if(tool == "print_SQL_Ausgabe"):
            testprint(dbc, table)
        elif(tool == "DBinCSV"):
            export_to_csv(dbc, table)
        elif(tool == "DBausgabeFenster"):
            read_from_database(dbc, table)
        elif(tool == "CSV_to_XML"):
            convert_csv_to_xml()
        elif(tool == "XML_to_CSV"):
            convert_xml_to_csv()
            

create_dropdown_login() #create gui
root.mainloop() #Execute tkinter mainloop