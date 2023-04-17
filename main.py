#!/usr/bin/env python3

import os
import csv
import time
import datetime
from typing import List


class Company:
    
    def __init__(self, name: str, occupation: str = None, address: str = None, web_page: str = None) -> None:
        self.name: str = name
        self.occupation: str = occupation or None
        self.address: str = address or None
        self.web_page: str = web_page or None
        
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
    
    def __init__(self, name: str, birthday: str = None, notes: str = None) -> None:
        self.name: str = name
        self.birthday: str = birthday or None
        self.notes: str = notes or None
        
    def __str__(self) -> str:
        representation = f"Name: {self.name}\n"
        
        if self.birthday:
            representation += f"Birthday: {self.birthday}\n"
            
        if self.notes:
            representation += f"Notes: {self.notes}\n"
            
        return representation
        

class Child:
    
    def __init__(self, name: str, birthday: str = None, notes: str = None) -> None:
        self.name: str = name
        self.birthday: str = birthday or None
        self.notes: str = notes or None
        
    def __str__(self) -> str:
        representation = f"Name: {self.name}\n"
        
        if self.birthday:
            representation += f"Birthday: {self.birthday}\n"
            
        if self.notes:
            representation += f"Notes: {self.notes}\n"
            
        return representation


class Contact:
    def __init__(self, name: str, mobile_phone: str, company: Company = None, mobile_phone2: str = None, mobile_phone3: str = None, home_phone: str = None, office_phone: str = None, private_email1: str = None, private_email2: str = None, office_email: str = None, melody: str = None, other_address: str = None, birthday: str = None, notes: str = None, spouse: Spouse = None, children: List[Child] = None):
        
        self.name: str = name
        self.mobile_phone: str = mobile_phone
        self.company: Company = company or None
        self.mobile_phone2: str = mobile_phone2 or None
        self.mobile_phone3: str = mobile_phone3 or None
        self.home_phone: str = home_phone or None
        self.office_phone: str = office_phone or None
        self.private_email1: str = private_email1 or None
        self.private_email2: str = private_email2 or None
        self.office_email: str= office_email or None
        self.melody: str = melody or None
        self.other_address: str = other_address or None
        self.birthday: str = birthday or None
        self.notes: str = notes or None
        self.spouse: Spouse = spouse or None
        self.children: List[Child] = children or None
        
    def __str__(self) -> str:
        representation = f"Name: {self.name}\nMobile Phone: {self.mobile_phone}\n"
        
        if self.company:
            representation += f"Company:\n{self.company}\n"
            
        if self.mobile_phone2:
            representation += f"Mobile Phone 2: {self.mobile_phone2}\n"
            
        if self.mobile_phone3:
            representation += f"Mobile Phone 3: {self.mobile_phone3}\n"
            
        if self.home_phone:
            representation += f"Home Phone: {self.home_phone}\n"
            
        if self.office_phone:
            representation += f"Office Phone: {self.office_phone}\n"
            
        if self.private_email1:
            representation += f"Private Email 1: {self.private_email1}\n"
            
        if self.private_email2:
            representation += f"Private Email 2: {self.private_email2}\n"
            
        if self.office_email:
            representation += f"Office Email: {self.office_email}\n"
            
        if self.melody:
            representation += f"Melody: {self.melody}\n"
            
        if self.other_address:
            representation += f"Other Address: {self.other_address}\n"
            
        if self.birthday:
            representation += f"Birthday: {self.birthday}\n"
            
        if self.notes:
            representation += f"Note: {self.notes}\n"
        
        if self.spouse:
            representation += f"Spouse:\n{self.spouse}\n"
        
        if self.children:
            for child in self.children:
                representation += f"Child:\n{child}\n"
            
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
                
                for i in range(-1, 19, -3):
                    children.append(row[i + 2], row[i + 1], row[i])
                    
                contact = Contact(row[0], row[1], company, row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], spouse, children)
                self.add_contact(contact)
                
            print(f"\nImporting contacts from {file_path} was succesfull!")
                
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
        for contact in self.contacts:
            print(f"{contact}\n")
        
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
    main_screen: str = str("Welcome to the Python 3 CLI Contact List!\n\n")
    
    while True:
        clear()
        print(main_screen + "1) Contact Actions\n2) Group Actions\n3) Exit")
        choice_layer_1 = str(input("\nEnter a number of choice: """))
        
        if choice_layer_1 == "1":
            while True:
                clear()
                print(main_screen + "1) Add a new contact\n2) Update an existing contact\n3) Delete an existing contact\n4) Search for an existing contact\n5) Birthday reminders\n6) Import contact list\n7) Export contact list\n8) Print all contacts\n9) Print specific contact\n10) Back")
                choice_layer_2 = str(input("\nEnter a number of choice: "))
                
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
                            print(f"Invalid values for either of the required name or mobile number details!\nTry again in {i} seconds ...")
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
                                print(f"Invalid value for company details!\nTry again in {i} seconds ...")
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
                    except TypeError:
                        pass
                            
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
                            
                            if children:
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
                
                # TODO: Update an existing contact
                elif choice_layer_2 == "2":
                    clear()
                    contact_name = input("Updating an existing contact ...\n\nWhich contact would you wish to update? ")
                    contacts = contact_book.search_contacts(contact_name)
                    
                    if len(contacts) > 0:
                        attribute = int(print("Which contact would you wish to update? "))
                    else:
                        clear()
                        print(f"No contacts with name {contact_name} found!\nTry again in {i} seconds ...")
                        time.sleep(1)
                        
                # TODO: Delete an existing contact
                elif choice_layer_2 == "3":
                    pass
                
                # Searh for an existing contact
                elif choice_layer_2 == "4":
                    clear()
                    contact_name = input("Updating an existing contact ...\n\nWhich contact would you wish to update? ")
                    results = contact_book.search_contacts(str(input("Searching for an existing contact ...\nEnter contact name: ")))
                    
                    for result in results:
                        print(result)
                    else:                        
                        for i in range(3, 0, -1):
                            clear()
                            print(f"No contacts with name {contact_name} found!\nTry again in {i} seconds ...")
                            time.sleep(1)
                        
                elif choice_layer_2 == "5":
                    pass
                
                # Import contact list
                elif choice_layer_2 == "6":
                    clear()
                    file_path = str(input("Importing contacts ...\n\nFrom which file would you wish to import contacts?\n> "))
                    contact_book.import_contacts(file_path)
                    
                    # try:
                    # except:
                    #     for i in range(3, 0, -1):
                    #         clear()
                    #         print(f"Something went wrong!\nTry again in {i} seconds ...")
                    #         time.sleep(1)
                    
                elif choice_layer_2 == "7":
                    pass
                elif choice_layer_2 == "8":
                    contact_book.print_contact_list()
                elif choice_layer_2 == "9":
                    pass
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
            print("Thank you for using Python 3 CLI Contact List!")
            break
        else:
            for i in range(3, 0, -1):
                clear()
                print(f"Invalid choice value!\nTry again in {i} seconds ...")
                time.sleep(1)

    search_query = input("Enter search query: ")
    search_results = contact_book.search_contacts(search_query)
    print(search_results)

    contact_id = input("Enter contact ID to update: ")
    update_field = input("Enter field to update: ")
    update_value = input("Enter new value: ")
    contact_book.update_contact(contact_id, {update_field: update_value})

    contact_list_filename = input("Enter contact list filename: ")
    contact_book.print_contact_list(contact_list_filename)

    contact_id = input("Enter contact ID to print details: ")
    contact_details_filename = input("Enter contact details filename: ")
    contact_book.print_contact_details(contact_id, contact_details_filename)

if __name__ == "__main__":
    main()
