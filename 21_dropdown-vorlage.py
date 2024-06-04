import tkinter as tk
from tkinter import ttk, StringVar, Label, Button, Entry, OptionMenu #Grafik-Bib
import subprocess # Andere Pythonprgramme ausführen

mitarbeiter_options=["Lager", "Verwaltung", "Marketing", "Geschäftsführung"] # Nutzer Gruppenspezifisch für Login

root = tk.Tk()
root.geometry("300x200") #Adjust window size

department_var = tk.StringVar()
passw_var = tk.StringVar()
status_var = tk.StringVar()

def create_dropdown_login():

    root.geometry("300x200") #Adjust window size
    department_var.set("Abteilung") #initial menu text
    
    #Create Dropdown menu 
    drop_label = Label(root, text = "Abteilung: ", font = ('calibre',10,'bold'))
    dropdown = OptionMenu(root, department_var, *mitarbeiter_options) 

    #Create password input
    passw_label = Label(root, text = 'Password: ', font = ('calibre',10,'bold'), justify="center")
    passw_entry = Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*', width="15")

    #Create button, it will change label text 
    login_button = Button(root, text = "Login", command = submit)

    status_label = Label(root, textvariable=status_var, font = ('calibre',10,'normal'), justify="left", wraplength=170)

    #create grid layout
    drop_label.grid(row=0, column=0, sticky="w")
    dropdown.grid(row=0, column=1, sticky="w")
    passw_label.grid(row=1, column=0, sticky="w")
    passw_entry.grid(row=1, column=1, sticky="w")
    login_button.grid(row=2, column=1, sticky="w")
    status_label.grid(row=3, column=1, sticky="w")
  
    root.mainloop() #Execute tkinter 
    #submit password

def submit():
    department = department_var.get()
    password = passw_var.get()

    if(department not in mitarbeiter_options):
        status_var.set("Bitte wählen sie eine Abteilung!")
    elif(password == ""):
        status_var.set("Bitte geben sie ein Password ein!")
    elif(password != department):
        status_var.set("Falsches Passwort!")
    elif(password == department):
        status_var.set("Erfolgreich eingeloggt!")

create_dropdown_login()