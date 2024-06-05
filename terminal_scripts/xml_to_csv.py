import sys
import os
import csv
import xml.etree.ElementTree as ET

def convert_xml_to_csv(xml_filepath, csv_filepath):
    tree = ET.parse(xml_filepath)  # XML-Datei parsen
    root = tree.getroot()  # Wurzelelement des XML-Baums erhalten

    data_element = root.find('Daten')
    if data_element is None:
        print(f"Fehler: Kein 'Daten'-Element in der Datei {xml_filepath} gefunden.")
        return

    # Kopfzeilen aus dem ersten 'Daten'-Element extrahieren
    headers = [elem.tag for elem in data_element]
    
    with open(csv_filepath, 'w', newline='') as csv_file:  # CSV-Datei im Schreibmodus öffnen
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(headers)  # Kopfzeilen in die CSV-Datei schreiben
        
        for record in root.findall('Daten'):  # Alle 'Daten'-Elemente durchlaufen
            row = [record.find(h).text if record.find(h) is not None else '' for h in headers]
            csv_writer.writerow(row)  # Jede Zeile in die CSV-Datei schreiben

# Alle XML-Dateien im Verzeichnis in CSV-Dateien konvertieren
directory = './xml/'
for filename in os.listdir(directory):
    fullPath = os.path.join(directory, filename)
    base, ext = os.path.splitext(filename)
    if os.path.isfile(fullPath) and ext.lower() == '.xml':
        convert_xml_to_csv(fullPath, f"./csv/{base}.csv")
