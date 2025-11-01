# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 20:32:04 2025

@author: Owner
"""

file_path = "maintenance_log.txt"

def add_to_records():
    with open(file_path,'a') as file:
        vehicle_id = input("Enter Vehicle ID or name: ")
        service_type = input("Enter service type (oil change, air filter replacement, etc.): ")
        mileage = input("Enter vehicle mileage: ")
        date = input("Enter date of service (MM/DD/YYYY): ")
        
        file.write(f"\n{vehicle_id}, {service_type}, {mileage}, {date}\n")
        
        print("\nMaintenance log record was successfully created.\n")
        
    
def view_records():
    try:
        with open(file_path, 'r') as file:
            records = file.readlines()
            if not records:
                print("\nNo previos records found.\n")
            else:
                print("--Vehicle Maintenance History--")
                for line in records:
                    print(line.strip())                   
    
    except FileNotFoundError:
        print("Maintenance log history was not found. Add a record first.\n")
        
def clear_records():
    delete_option = input("Are you sure you would like to delete all previous records? (yes or no): ").lower()
    if delete_option == "yes":
        with open(file_path, "w") as file:
            file.truncate(0)            ##Deletes writings starting from very first point
            print("\nMaintenance records have been deleted")
    else:
        print("Deletion of Maintenance file data has been canceled.")
            
def main():
    while True:
        print("----Vehicle Maintenance Tracker----")
        print("1. Add Maintenance record")
        print("2. View Maintenance Record History")
        print("3. Clear Maintenance file records")
        print("4. Exit")
        
        user_choice = input("Select an option (1-4): ")
        

        if user_choice == "1":
            add_to_records()
        elif user_choice == "2":
            view_records()
        elif user_choice == "3":
            clear_records()
        elif user_choice == "4":
            print("Exiting Program...")
            break
        else:
            print("\nInvalid Menu Option. Please select options (1-4)\n")
        
main()

        
            
    
        
        
        
        
        
        