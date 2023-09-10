import os

try:
    import biplist
except ImportError:
    print("'biplist' not found. Installing...")
    try:
        os.system("pip install biplist")
        import biplist
        print("'biplist' successfully installed.")
    except Exception as install_error:
        print(f"Failed to install 'biplist': {install_error}")
        exit(1)

input_path = input("Input file path: ").strip()

if os.path.isfile(input_path):
    try:
        plist_data = biplist.readPlist(input_path)
        
        translations = {orig.replace("\n", "\\n"): translate.replace("\n", "\\n") for orig, translate in plist_data.items()}
    
        output_path = os.path.splitext(input_path)[0] + " (new).strings"
        
        with open(output_path, 'w', encoding='utf-8') as output_file:
            for orig, translate in translations.items():
                output_file.write(f'"{orig}" = "{translate}";\n')
        
        print(f"File saved as {output_path}")
    
    except Exception as e:
        print(f"Failed to process file: {e}")
else:
    print(f"'{input_path}' not found.")
