import csv
import xml.etree.ElementTree as ET

def convert_csv_to_xml(csv_filepath, xml_filepath):
    with open(csv_filepath, 'r') as csv_file: #CSV wird im Lesemodus geöffnet 
        csv_reader = csv.reader(csv_file) #erstellt einen csv reader um die csv Inhalt zu lesen
        headers = next(csv_reader) #Liest die Kopfzeile als Spalteüberschrift
        
        root = ET.Element('Tabelle')   # Wurzelelement des XML-Baums mit dem Namen 'Tabelle'.
        for row in csv_reader:      #geht durch jede Zeile der CSV-Datei
            record = ET.SubElement(root, 'Daten')  #Unterelement unter dem Wurzelelement mit dem Namen 'Daten'.
            for h, val in zip(headers, row): #geht durch jedes Element des CSV-Datei
                ET.SubElement(record, h).text = val 
                    
        tree = ET.ElementTree(root) #erstellt einen ElementTree
        tree.write(xml_filepath) #Speichert den ElementTree

    tree = ET.ElementTree(root) 
    tree.write(xml_filepath, encoding='utf-8', xml_declaration=True)  


# Beispiel: CSV-Datei in XML konvertieren
convert_csv_to_xml(r"C:\Users\ISRA\Desktop\csv\daten.csv", r"C:\Users\ISRA\Desktop\csv\xml_output.xml") #r schreibt die Daten in Raw format
