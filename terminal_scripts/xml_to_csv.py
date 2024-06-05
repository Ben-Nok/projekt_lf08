import sys
import os
import csv
import xml.etree.ElementTree as ET

def convert_xml_to_csv(xml_filepath, csv_filepath):
    try:
        tree = ET.parse(xml_filepath)  # XML-Datei parsen
        root = tree.getroot()  # Wurzelelement des XML-Baums erhalten

        # Kopfzeilen aus dem ersten 'Daten'-Element extrahieren
        headers = [elem.tag for elem in root.find('Daten')]
        
        with open(csv_filepath, 'w', newline='') as csv_file:  # CSV-Datei im Schreibmodus öffnen
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(headers)  # Kopfzeilen in die CSV-Datei schreiben
            
            for record in root.findall('Daten'):  # Alle 'Daten'-Elemente durchlaufen
                row = [record.find(h).text if record.find(h) is not None else '' for h in headers]
                csv_writer.writerow(row)  # Jede Zeile in die CSV-Datei schreiben
    except ET.ParseError as e:
        print(f"Fehler beim Parsen der Datei {xml_filepath}: {e}")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

# Verzeichnisse überprüfen und erstellen
input_directory = './xml/'
output_directory = './csv/'
os.makedirs(output_directory, exist_ok=True)

# Alle XML-Dateien im Verzeichnis in CSV-Dateien konvertieren
for filename in os.listdir(input_directory):
    fullPath = os.path.join(input_directory, filename)
    base, ext = os.path.splitext(filename)
    if os.path.isfile(fullPath) and ext.lower() == '.xml':
        convert_xml_to_csv(fullPath, os.path.join(output_directory, f"{base}.csv"))
