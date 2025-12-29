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
    with open("contacts.json", "w") as j_file:
        json.dump([contact.to_dictionary() for contact in contacts], j_file, indent=4)
        
    with open("report.csv", "w", newline="") as c_file:
        writer = csv.writer(c_file)
        writer.writerow(["name", "surname", "phone", "email"])
        writer.writerows([contact.to_list() for contact in contacts])
        
def load_from_json():
    try:
        with open("contacts.json", "r") as f:
            data = json.load(f)
            return [Contact(d["name"], d["surname"], d["phone"], d["email"]) for d in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def main():
    contacts = load_from_json()
    while True:
        print("1. Add Contact 2. View Contacts 3. Exit ")
        try:
            choice = input("select: ")
            
            if choice == "1":
                name = input("Name: ").strip().title()
                surname = input("Surname: ").strip().title()
                phone = input("Phone: ").strip()
                email = input("Email: ").strip()
                
                contacts.append(Contact(name, surname, phone, email))
                save_all(contacts)
                
            elif choice == "2":
                print("\n --- Contact list ---")
                for item in contacts:
                    print(f"{item.name}\n {item.surname}\n {item.phone}\n {item.email}")
            elif choice == "3":
                print("Exiting the contact manager")
                break
        except ValueError:
            print("incorrect selection")
        break

main()