import sys
import os
import csv
import xml.etree.ElementTree as ET

def convert_file(xml_filepath, csv_filepath):
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

    print(f"{xml_filepath} erfolgreich zu {csv_filepath} konvertiert")
def convert_xml_to_csv():
    # Alle XML-Dateien im Verzeichnis in CSV-Dateien konvertieren
    directory = './exports/xml/'
    os.makedirs(os.path.dirname("./exports/xml_converted_csv/"), exist_ok=True) #create directory
    for filename in os.listdir(directory):
        fullPath = os.path.join(directory, filename)
        base, ext = os.path.splitext(filename)
        if os.path.isfile(fullPath) and ext.lower() == '.xml':
            convert_file(fullPath, f"./exports/xml_converted_csv/{base}.csv")
