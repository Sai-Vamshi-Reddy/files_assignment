import os
import json
import csv

# Function to open a JSON file from the given path
def open_json_file(file_path="sai_vamshi_adoptions.json"):
    try:
        file = open(file_path, 'r')
        data = json.load(file)
        file.close()
        print("File loaded successfully.")
        return data

    except FileNotFoundError:
        print("File not found. Please check the path.")
    except json.JSONDecodeError:
        print("Error reading JSON. Check the file format.")
    except Exception as e:
        print("An error occurred:", e) 