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

 # Function to save the contacts data to a CSV file
def save_contacts_to_csv(data):
    if data is None:
        return

    file = open('sai_vamshi_contacts.csv', mode='w', newline='')
    writer = csv.writer(file)
    writer.writerow(['Contact Order', 'Gender', 'First Name', 'Last Name'])

    for record in data:
        for contact in record['contacts']:
            writer.writerow([
                contact['order'],
                contact['gender'],
                contact['firstname'],
                contact['lastname']
            ])

    file.close()
    print("Contact data saved to CSV.")
 
 # Function to save the adoptions data to a CSV file
def save_adoptions_to_csv(data):
    if data is None:
        return

    file = open('sai_vamshi_adoptions.csv', mode='w', newline='')
    writer = csv.writer(file)
    writer.writerow(['Adoption ID', 'Date', 'Quantity', 'Book Id', 'Book Title', 'Category'])

    for record in data:
        for adoption in record['adoptions']:
            writer.writerow([
                adoption['id'],
                adoption['date'],
                adoption['quantity'],
                adoption['book']['id'],
                adoption['book']['title'],
                adoption['book']['category']
            ])

    file.close()
    print("Adoption data saved to CSV.") 

# Function to save the messages data to a CSV file
def save_messages_to_csv(data):
    if data is None:
        return

    file = open('sai_vamshi_messages.csv', mode='w', newline='')
    writer = csv.writer(file)
    writer.writerow(['Message ID', 'Message Date', 'Content', 'Category'])

    for record in data:
        for message in record['messages']:
            writer.writerow([
                message['id'],
                message['date'],
                message['content'],
                message['category']
            ])

    file.close()
    print("Message data saved to CSV.") 

def save_all_data_to_csv(data):
    save_universities_to_csv(data)
    save_contacts_to_csv(data)
    save_adoptions_to_csv(data)
    save_messages_to_csv(data)


# Function to list universities based on the state
def list_universities_by_state(data, state_name):
    if data is None:
        print("No data available.")
        return

    found_university = False
    print("Universities in", state_name, ":")

    for record in data:
        university = record['university']
        if university['state'] == state_name:
            print(university['name'])
            found_university = True

    if not found_university:
        print("No universities found in", state_name)


# Function to save book titles in a specific category to a text file
def save_books_by_category(data, category_choice):
    if data is None:
        print("No data available.")
        return

    found_book = False
    file = open(category_choice + '_books.txt', mode='w')

    for record in data:
        for adoption in record['adoptions']:
            if adoption['book']['category'] == category_choice:
                file.write(adoption['book']['title'] + '\n')
                found_book = True

    file.close()

    if not found_book:
        print("No books found in the category:", category_choice)
    else:
        print("Books in the '" + category_choice + "' category saved to a text file.")


def demonstrate_function():
    file_path = input("Enter the file path of the JSON file: ")
    data = open_json_file(file_path)

    if data is not None:
        state = input("Enter a state name to list universities: ")
        list_universities_by_state(data, state)

        category_choice = input("Enter a category to save book titles: ")
        save_books_by_category(data, category_choice)
        save_all_data_to_csv(data)

if __name__ == "__main__":
    demonstrate_function()
