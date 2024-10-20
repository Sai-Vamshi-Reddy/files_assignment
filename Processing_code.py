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

# Function to save the adoption data to a CSV file
def save_universities_to_csv(data):
    if data is None:
        return

    file = open('sai_vamshi_universities.csv', mode='w', newline='')
    writer = csv.writer(file)
    writer.writerow(['University ID', 'University Name', 'Address', 'City', 'State', 'Website', 'Zip','Longitude','Latitude','Classification'])

    for record in data:
        university = record['university']
        writer.writerow([
            university['id'],
            university['name'],
            university.get('address', 'N/A'),
            university['city'],
            university['state'],
            university.get('website', 'N/A'),
            university['zip'],
            university['longitude'],
            university['latitude'],
            university['classification']
        ])

    file.close()
    print("University data saved to CSV.")
 