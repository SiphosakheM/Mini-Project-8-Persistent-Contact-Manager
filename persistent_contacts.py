import json
import csv

class Contact:
    def __init__(self, name , surname , phone , email):
        self.name = name 
        self.surname = surname
        self.phone = phone
        self.email = email
        
    def  to_dictionary(self):
        return{"name":self.name, "surname": self.surname, "phone":self.phone, "email": self.email }
    
    def to_list(self):
        return[self.name, self.surname, self.phone, self.email]
    
def save_all(contacts):
    with open("contacts.json", "w", encoding="utf-8") as j_file:
        json.dump([contact.to_dictionary() for contact in contacts], j_file, indent=4)
        
    with open("report.csv", "w", newline="", encoding="utf-8") as c_file:
        writer = csv.writer(c_file)
        writer.writerow(["name", "surname", "phone", "email"])
        writer.writerows([contact.to_list() for contact in contacts])
        
def load_from_json():
    try:
        with open("contacts.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Contact(d["name"], d["surname"], d["phone"], d["email"]) for d in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

contacts = load_from_json()