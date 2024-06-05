import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import csv, os
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def convert_csv_to_xml(csv_filepath, xml_filepath):
    with open(csv_filepath, 'r') as csv_file: #CSV wird im Lesemodus geöffnet 
        csv_reader = csv.reader(csv_file) #erstellt einen csv reader um die csv Inhalt zu lesen
        headers = next(csv_reader) #Liest die Kopfzeile als Spalteüberschrift
        
        root = ET.Element('Tabelle')   # Wurzelelement des XML-Baums mit dem Namen 'Tabelle'.
        for row in csv_reader:      #geht durch jede Zeile der CSV-Datei
            record = ET.SubElement(root, 'Daten')  #Unterelement unter dem Wurzelelement mit dem Namen 'Daten'.
            for h, val in zip(headers, row): #geht durch jedes Element des CSV-Datei
                ET.SubElement(record, h).text = val 
    
    reparsed = minidom.parseString(ET.tostring(root, 'utf-8')) #parse string to a DOM
    xml_content = reparsed.toprettyxml(indent="  ")#format parsed string to a readable xml format
    
    os.makedirs(os.path.dirname("./xml/"), exist_ok=True) #create xml directory
    with open(xml_filepath, "w") as file: #write file to xml directory
        file.write(xml_content)
