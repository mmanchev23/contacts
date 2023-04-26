#!/usr/bin/env python3

import os
import csv
import time
import datetime
from typing import List


class Company:
    
    def __init__(self, name: str, occupation: str = "No information given ...", address: str = "No information given ...", web_page: str = "No information given ...") -> None:
        self.name: str = name
        self.occupation: str = occupation or "No information given ..."
        self.address: str = address or "No information given ..."
        self.web_page: str = web_page or "No information given ..."
        
    def __str__(self) -> str:
        representation = f"Name: {self.name}\n"
        
        if self.occupation:
            representation += f"Occupation: {self.occupation}\n"
            
        if self.address:
            representation += f"Address: {self.address}\n"
            
        if self.web_page:
            representation += f"Web Page: {self.web_page}"
            
        return representation


class Spouse:
    
    def __init__(self, name: str, birthday: str = "No information given ...", notes: str = "No information given ...") -> None:
        self.name: str = name
        self.birthday: str = birthday or "No information given ..."
        self.notes: str = notes or "No information given ..."
        
    def __str__(self) -> str:
        representation = f"Name: {self.name}\n"
        
        if self.birthday:
            representation += f"Birthday: {self.birthday}\n"
            
        if self.notes:
            representation += f"Notes: {self.notes}\n"
            
        return representation
        

class Child:
    
    def __init__(self, name: str, birthday: str = "No information given ...", notes: str = "No information given ...") -> None:
        self.name: str = name
        self.birthday: str = birthday or "No information given ..."
        self.notes: str = notes or "No information given ..."
        
    def __str__(self) -> str:
        representation = f"Name: {self.name}\n"
        
        if self.birthday:
            representation += f"Birthday: {self.birthday}\n"
            
        if self.notes:
            representation += f"Notes: {self.notes}\n"
            
        return representation


class Contact:
    def __init__(self, name: str, mobile_phone: str, company: Company = None, mobile_phone2: str = "No information given ...", mobile_phone3: str = "No information given ...", home_phone: str = "No information given ...", office_phone: str = "No information given ...", private_email1: str = "No information given ...", private_email2: str = "No information given ...", office_email: str = "No information given ...", melody: str = "No information given ...", other_address: str = "No information given ...", birthday: str = "No information given ...", notes: str = "No information given ...", spouse: Spouse = None, children: List[Child] = list()) -> None:
        
        self.name: str = name
        self.mobile_phone: str = mobile_phone
        self.company: Company = company or None
        self.mobile_phone2: str = mobile_phone2 or "No information given ..."
        self.mobile_phone3: str = mobile_phone3 or "No information given ..."
        self.home_phone: str = home_phone or "No information given ..."
        self.office_phone: str = office_phone or "No information given ..."
        self.private_email1: str = private_email1 or "No information given ..."
        self.private_email2: str = private_email2 or "No information given ..."
        self.office_email: str= office_email or "No information given ..."
        self.melody: str = melody or "No information given ..."
        self.other_address: str = other_address or "No information given ..."
        self.birthday: str = birthday or "No information given ..."
        self.notes: str = notes or "No information given ..."
        self.spouse: Spouse = spouse or None
        self.children: List[Child] = children or list()
        
    def __str__(self) -> str:
        representation = f"Name: {self.name}\nMobile Phone: {self.mobile_phone}\n\n"
        
        if self.company.name is not "":
            representation += f"Company Details:\n{self.company}\n\n"
        else:
            representation += f"Company Details:\nNo company information given ...\n\n"
            
        if self.mobile_phone2:
            representation += f"Mobile Phone 2: {self.mobile_phone2}\n"
            
        if self.mobile_phone3:
            representation += f"Mobile Phone 3: {self.mobile_phone3}\n"
            
        if self.home_phone:
            representation += f"Home Phone: {self.home_phone}\n"
            
        if self.office_phone:
            representation += f"Office Phone: {self.office_phone}\n\n"
            
        if self.private_email1:
            representation += f"Private Email 1: {self.private_email1}\n"
            
        if self.private_email2:
            representation += f"Private Email 2: {self.private_email2}\n"
            
        if self.office_email:
            representation += f"Office Email: {self.office_email}\n\n"
            
        if self.melody:
            representation += f"Melody: {self.melody}\n"
            
        if self.other_address:
            representation += f"Other Address: {self.other_address}\n"
            
        if self.birthday:
            representation += f"Birthday: {self.birthday}\n"
            
        if self.notes:
            representation += f"Note: {self.notes}\n\n"
        
        if self.spouse:
            representation += f"Spouse Details:\n{self.spouse}\n\n"
        
        if len(self.children) > 0:
            for child in self.children:
                representation += f"Child Details:\n{child}\n"
        else:
            representation += f"Child Details:\nNo children information given ...\n"
            
        return representation


class ContactBook:
    
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_contacts(self, name):
        results = []
        
        for contact in self.contacts:
            if name in contact.name:
                results.append(contact)
            else:
                print(f"No contacts with name {name} found!")
                return
                
        return results

    def update_contact(self, contact, updated_info):
        for key, value in updated_info.items():
            setattr(contact, key, value)

    def delete_contact(self, contact):
        self.contacts.remove(contact)

    def create_contact_group(self, group_name):
        group = []
        setattr(self, group_name, group)

    def add_contact_to_group(self, contact, group_name):
        if hasattr(self, group_name):
            group = getattr(self, group_name)
            group.append(contact)
        else:
            print("Group not found.")

    def delete_contact_from_group(self, contact, group_name):
        if hasattr(self, group_name):
            group = getattr(self, group_name)
            
            if contact in group:
                group.remove(contact)
            else:
                print("Contact not found in the group.")
        else:
            print("Group not found.")

    def get_birthday_reminders(self):
        today = datetime.now().strftime("%m/%d")
        reminders = []
        
        for contact in self.contacts:
            if contact.birthday == today:
                reminders.append(contact)
                
        return reminders

    def import_contacts(self, file_path):
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            
            for row in reader:
                company = Company(row[2], row[3], row[4], row[5])
                spouse = Spouse(row[17], row[18], row[19])
                children = list()
                
                for i in range(20, len(row), 3):
                    if i + 2 < len(row):
                        children.append(Child(row[i], row[i + 1], row[i + 2]))
                    
                contact = Contact(row[0], row[1], company, row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], spouse, children)
                self.add_contact(contact)
                
            print(f"\nImporting contacts from {file_path} ...")
                
            time.sleep(3)

    def export_contacts(self, file_path):
        with open(file_path, "w") as file:
            writer = csv.writer(file)
            
            for contact in self.contacts:
                writer.writerow([contact.name, contact.mobile_phone, contact.company_name,
                                 contact.occupation, contact.address, contact.web_page,
                                 contact.mobile_phone2, contact.mobile_phone3, contact.home_phone,
                                 contact.office_phone, contact.private_email1, contact.private_email2,
                                 contact.office_email, contact.melody, contact.other_address,
                                 contact.birthday, contact.notes, contact.spouse, contact.children])

    def print_contact_list(self):
        if len(self.contacts) > 0:
            for contact in self.contacts:
                print(f"{contact}\n")
        else:
            print("No contacts found!\n")
            
        input("Press any key to continue ...")

    def print_contact_details(self, contact, file_path):
        with open(file_path, "w") as file:
            file.write("Contact Details:\n")
            file.write(f"Name: {contact.name}\n")
            file.write(f"Mobile Phone: {contact.mobile_phone}\n")
            file.write(f"Company Name: {contact.company_name}\n")
            file.write(f"Occupation: {contact.company_occupation}\n")
            file.write(f"Address: {contact.company_address}\n")
            file.write(f"Website: {contact.company_web_page}\n")
            file.write(f"Mobile Phone 2: {contact.mobile_phone2}\n")
            file.write(f"Mobile Phone 3: {contact.mobile_phone3}\n")
            file.write(f"Home Phone: {contact.home_phone}\n")
            file.write(f"Office Phone: {contact.office_phone}\n")
            file.write(f"Private Email 1: {contact.private_email1}\n")
            file.write(f"Private Email 2: {contact.private_email2}\n")
            file.write(f"Office Email: {contact.office_email}\n")
            file.write(f"Melody: {contact.melody}\n")
            file.write(f"Other Address: {contact.other_address}\n")
            file.write(f"Birthday: {contact.birthday}\n")
            file.write(f"Notes: {contact.notes}\n")
            
            if contact.spouse_name and contact.spouse_birthday and contact.spouse_notes:
                file.write(f"Spouse: {contact.spouse.name} {contact.spouse.birthday} {contact.spouse.notes}\n")
                
            if contact.children:
                for child in contact.children:
                    file.write(f"Child: {child.name} {child.birthday} {child.notes}\n")


def main() -> None:
    contact_book = ContactBook()
    clear = lambda: os.system("cls") if os.name == "nt" else os.system("clear")
    main_screen: str = str("Welcome to the Python 3 CLI Contact Manager!\n\n")
    
    while True:
        clear()
        choice_layer_1 = str(input(main_screen + 
        "1) Contact Actions\n"
        "2) Group Actions\n"
        "3) Exit\n"
        "\nEnter a number of choice: "))
        
        if choice_layer_1 == "1":
            while True:
                clear()
                choice_layer_2 = str(input(main_screen +
                "1) Add a new contact\n"
                "2) Update an existing contact\n"
                "3) Delete an existing contact\n"
                "4) Search for an existing contact\n"
                "5) Birthday reminders\n"
                "6) Import contact list\n"
                "7) Export contact list\n"
                "8) Print all contacts\n"
                "9) Print specific contact\n"
                "10) Back\n"
                "\nEnter a number of choice: "))
                
                # Add a new contact
                if choice_layer_2 == "1":
                    clear()
                    contact = Contact(name=None, mobile_phone=None)
                    company = Company(name=None)
                    spouse = Spouse(name=None)
                    children = list()
                    print("Adding new contact ...\n[!] - Required\n[+] - Optional\n")
                    
                    try:
                        contact.name = str(input("[!] Enter name: "))
                        contact.mobile_phone = str(input("[!] Enter phone number: "))
                    except:
                        for i in range(3, 0, -1):
                            clear()
                            print(f"Invalid personal details!\nTry again in {i} seconds ...")
                            time.sleep(1)
                            
                    if str(input("\nDoes the contact has/works in a company? [Y/N] ")) in ["Yes", "Y", "yes", "y"]:
                        try:
                            company.name = str(input("[!] Enter company name: "))
                            company.occupation = str(input("[+] Enter company occupation: "))
                            company.address = str(input("[+] Enter company address: "))
                            company.web_page = str(input("[+] Enter company web page: "))
                            
                            if company.name:
                                contact.company = company
                        except:
                            for i in range(3, 0, -1):
                                clear()
                                print(f"Invalid company details!\nTry again in {i} seconds ...")
                                time.sleep(1)
                        
                    try:
                        contact.mobile_phone2 = str(input("[+] Enter phone number 2: "))
                        contact.mobile_phone3 = str(input("[+] Enter phone number 3: "))
                        contact.home_phone = str(input("[+] Enter home phone number: "))
                        contact.office_phone = str(input("[+] Enter work phone number: "))
                        contact.private_email1 = str(input("[+] Enter private email 1: "))
                        contact.private_email2 = str(input("[+] Enter private email 2: "))
                        contact.office_mail = str(input("[+] Enter office email: "))
                        contact.melody = str(input("[+] Enter melody: "))
                        contact.address = str(input("[+] Enter address: "))
                        contact.birthday = str(input("[+] Enter birthday: "))
                        contact.notes = str(input("[+] Enter notes: "))
                    except:
                        for i in range(3, 0, -1):
                            clear()
                            print(f"Invalid formal details!\nTry again in {i} seconds ...")
                            time.sleep(1)
                            
                    try:
                        if str(input("\n[+] Does the contact have a spouse? [Y/N] ")) in ["Yes", "Y", "yes", "y"]:
                            spouse.name = str(input("[!] Enter spouse name: "))
                            spouse.birthday = str(input("[+] Enter spouse birthday: "))
                            spouse.notes = str(input("[+] Enter spouse notes: "))
                            
                            if spouse.name:
                                contact.spouse = spouse
                    except:
                        for i in range(3, 0, -1):
                            clear()
                            print(f"Invalid spouse details!\nTry again in {i} seconds ...")
                            time.sleep(1)
                            
                    try:
                        if str(input("\n[+] Does the contact have any children? [Y/N] ")) in ["Yes", "Y", "yes", "y"]:
                            number_of_children = int(input("How many children does the contact have? "))
                            
                            if number_of_children > 0:
                                for _ in range(number_of_children):
                                    child_name = str(input("[!] Enter child name: "))
                                    child_birthday = str(input("[+] Enter child birthday: "))
                                    child_notes = str(input("[+] Enter child notes: "))
                                    child = Child(name=child_name, birthday=child_birthday, notes=child_notes)
                                    
                                    if child.name:
                                        children.append()
                            
                            if len(children) > 0:
                                contact.children = children
                    except:
                        for i in range(3, 0, -1):
                            clear()
                            print(f"Invalid children details!\nTry again in {i} seconds ...")
                            time.sleep(1)
                        
                    if contact.name and contact.mobile_phone:
                        contact_book.add_contact(contact=contact)
                        print("Contact added successfully!")
                        time.sleep(3)
                    else:
                        for i in range(3, 0, -1):
                            clear()
                            print(f"Something went wrong!\nTry again in {i} seconds ...")
                            time.sleep(1)
                
                # Update an existing contact
                elif choice_layer_2 == "2":
                    clear()
                    contact_name = str(input("Updating an existing contact ...\n\nWhich contact would you wish to update? "))
                    contacts = contact_book.search_contacts(contact_name)
                    
                    if len(contacts) > 0:
                        attribute_type = str(input("Which detail would you wish to update?\n> "))
                        attribute_value = str(input("New value: "))
                        contact_book.update_contact(contacts[0], { attribute_type: attribute_value })
                        print("Contact information updated successfully!")
                        time.sleep(3)
                    else:                        
                        for i in range(3, 0, -1):
                            clear()
                            print(f"No contacts with name {contact_name} found!\nTry again in {i} seconds ...")
                            time.sleep(1)
                        
                # Delete an existing contact
                elif choice_layer_2 == "3":
                    clear()
                    contact_name = str(input("Deleting an existing contact ...\n\nWhich contact would you wish to delete? "))
                    contacts = contact_book.search_contacts(contact_name)
                    
                    if len(contacts) > 0:
                        contact_book.delete_contact(contacts[0])
                        print("Contact deleted successfully!")
                        time.sleep(3)
                    else:                        
                        for i in range(3, 0, -1):
                            clear()
                            print(f"No contacts with name {contact_name} found!\nTry again in {i} seconds ...")
                            time.sleep(1)
                
                # Searh for an existing contact
                elif choice_layer_2 == "4":
                    clear()
                    results = contact_book.search_contacts(str(input("Searching for an existing contact ...\nEnter contact name: ")))
                    
                    for result in results:
                        print(result)
                    else:                        
                        for i in range(3, 0, -1):
                            clear()
                            print(f"No contacts with name {results} found!\nTry again in {i} seconds ...")
                            time.sleep(1)
                       
                # Birthday reminder functinality 
                elif choice_layer_2 == "5":
                    clear()
                    today = datetime.date.today()
                    
                    print(f"Birthdays reminder: {today}")
                    
                    try:
                        for contact in contact_book.contacts:
                            birthday = datetime.date(contact.birthday)
                            delta = birthday - today
                            
                            if delta.days < 10:
                                print(f"{delta.days} to {contact.name}'s birthday ...")
                            else:
                                continue
                    except:
                        for i in range(3, 0, -1):
                            clear()
                            print(f"Something went wrong!\nTry again in {i} seconds ...")
                            time.sleep(1)
                
                # Import contact list
                elif choice_layer_2 == "6":
                    try:
                        clear()
                        file_path = str(input("Importing contacts from \".csv\" file ...\n\nFrom which file would you wish to import contacts?\n\n(./test.csv) > "))
                        
                        if file_path:
                            contact_book.import_contacts(file_path)
                        else:
                            contact_book.import_contacts("./test.csv")
                    except:
                        for i in range(3, 0, -1):
                            clear()
                            print(f"Something went wrong!\nTry again in {i} seconds ...")
                            time.sleep(1)
                    
                # Export contact list
                elif choice_layer_2 == "7":
                    try:
                        clear()
                        file_path = str(input("Exporting contacts to \".csv\" file ...\n\nPlease specify a file name?\n\n(./test.csv) > "))
                        
                        if file_path:
                            contact_book.export_contacts(file_path)
                        else:
                            contact_book.export_contacts("./test.csv")
                    except:
                        for i in range(3, 0, -1):
                            clear()
                            print(f"Something went wrong!\nTry again in {i} seconds ...")
                            time.sleep(1)
                
                # Print all contacts
                elif choice_layer_2 == "8":
                    clear()
                    contact_book.print_contact_list()
                    
                # Print specific contact
                elif choice_layer_2 == "9":
                    try:
                        clear()
                        result = contact_book.search_contacts(str(input("Searching for an existing contact ...\nEnter contact name: ")))
                        file_path = str(input("Exporting contact to \".csv\" file ...\n\nPlease specify a file name?\n\n(./test.csv) > "))
                        
                        if file_path and result:
                            contact_book.print_contact_details(contact, file_path)
                        else:
                            contact_book.print_contact_details(contact, "./test.csv")
                    except:
                        for i in range(3, 0, -1):
                            clear()
                            print(f"Something went wrong!\nTry again in {i} seconds ...")
                            time.sleep(1)
                
                elif choice_layer_2 == "10":
                    break
                else:
                    for i in range(3, 0, -1):
                        clear()
                        print(f"Invalid choice value!\nTry again in {i} seconds ...")
                        time.sleep(1)              
        elif choice_layer_1 == "2":
            clear()
            print(main_screen + "1) Create a new contact\n2) Update an existing contact\n3) Delete an existing contact\n4) Searh for an existing contac\n5) Birthday reminders\n6) Import contact list\n7) Export contact list\n8) Print all contact\n9) Print specific contact")
        elif choice_layer_1 == "3":
            clear()
            print("Thank you for using Python 3 CLI Contact Manager!")
            break
        else:
            for i in range(3, 0, -1):
                clear()
                print(f"Invalid choice value!\nTry again in {i} seconds ...")
                time.sleep(1)

if __name__ == "__main__":
    main()
