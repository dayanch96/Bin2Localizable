import os
import subprocess
import plistlib

input_path = input("Input file path: ").strip()

if os.path.isfile(input_path):
    subprocess.run(["plutil", "-convert", "xml1", input_path])

    with open(input_path, 'rb') as xml_file:
        plist_data = plistlib.load(xml_file)
        translations = {orig.replace('\n', '\\n').replace('"', '\\"'): translate.replace('\n', '\\n').replace('"', '\\"') for orig, translate in plist_data.items()}

    output_path = os.path.splitext(input_path)[0] + " (new).strings"
    with open(output_path, 'w') as output_file:
        for orig, translate in translations.items():
            output_file.write(f'"{orig}" = "{translate}";\n')

    print(f"File saved as {output_path}")
else:
    print(f"'{input_path}' not found.")
