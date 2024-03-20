contacts ={}

def display_contact():
    print("Name\t\tContact Number\t\tEmail\t\tAddress ")
    for name, details in contacts.items():
        print(f"{name}\t\t{details[0]}\t\t{details[1]}\t\t{details[2]}")
        
def get_valid_phone_number():
    while True:
        phone = input("Enter your phone number(digits only):")
        if phone.isdigit():
            return phone
        else:
            print("Please enter only digits for the phone number. ")
        
while True:
    
    print("\nContact Management System")
    print("1. Add COntact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4.. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    
    if choice=="1":
        name= input("Enter contact name: ")
        phone = get_valid_phone_number()
        email = input ("Enter email: ")
        address = input ("Enter address: ")
        contacts[name]= [phone, email, address]
        print ("Contact added successfully! ")
        
    elif choice=="2":
        if not contacts:
            print("Contact list is empty. ")
        else:
            display_contact()
            
        
    elif choice == "3":
        search_term = input("Enter name or phone number to search: ")
        found = False
        for name, details in contacts.items():
            if search_term.lower() in name.lower() or search_term in details [0]:
                print("Contact found: ")
                print("Name:", name)
                print("Contact Number:", details[0])
                print("Email:", details[1])
                print("Address:", details[2])
                
                found = True
        if not found:
            print("No matching conatcts found.")
                
       
    elif choice == "4":
        edit_contact = input("Enter the contact to be eadited: ")
        if edit_contact in contacts:
            phone = get_valid_phone_number()
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contacts[edit_contact] = [phone, email, address]
            print("Contact update successfully!")
            
        else:
            print("Contact not found.")
            
        
    elif choice == "5": 
        del_contact = input("Enter the contact to be deleted: ")
        if del_contact in contacts:
            confirm = input("Do you want to delete this contact yes/no?: ")
            if confirm.lower() == "yes":
                del contacts [del_contact]
                print("Contact deleted successfully!")
            else:
                print("Contact not deleted.")
        else:
            print("Contact not found.")
    elif choice == "6":
        print("Exiting...")
        break
                
    else:
            print("Invalid choice. Please try again.")
    
            
            
            
            
        