# CarFinder - AutoCountry Vehicle Finder v0.5

FILENAME = "allowed_vehicles.txt"

import os
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as file:
        file.write('\n'.join([
            'Ford F-150',
            'Chevrolet Silverado',
            'Tesla CyberTruck',
            'Toyota Tundra',
            'Rivian R1T',
            'Ram 1500'
        ]))

def read_vehicles():
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def write_vehicles(vehicle_list):
    with open(FILENAME, "w") as file:
        file.write('\n'.join(vehicle_list))

def print_vehicles():
    vehicles = read_vehicles()
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for v in vehicles:
        print(v)

def search_vehicle():
    vehicles = read_vehicles()
    search = input("\nPlease Enter the full Vehicle name: ")
    if search in vehicles:
        print(f"\n'{search}' is an authorized vehicle!")
    else:
        print(f"\n'{search}' is not an authorized vehicle. If you received this in error, please check the spelling and try again.")

def add_vehicle():
    vehicles = read_vehicles()
    new_vehicle = input("\nPlease Enter the full Vehicle name you would like to ADD: ")
    if new_vehicle in vehicles:
        print(f"\n'{new_vehicle}' is already in the Authorized Vehicles List.")
    else:
        vehicles.append(new_vehicle)
        write_vehicles(vehicles)
        print(f"\nYou have added '{new_vehicle}' as an authorized vehicle.")

def delete_vehicle():
    vehicles = read_vehicles()
    del_vehicle = input("\nPlease Enter the full Vehicle name you would like to REMOVE: ")
    if del_vehicle in vehicles:
        confirm = input(f"Are you sure you want to remove '{del_vehicle}' from the Authorized Vehicles List? (yes/no): ").lower()
        if confirm == "yes":
            vehicles.remove(del_vehicle)
            write_vehicles(vehicles)
            print(f"\nYou have REMOVED '{del_vehicle}' as an authorized vehicle.")
        else:
            print("\nVehicle not removed.")
    else:
        print(f"\n'{del_vehicle}' is not in the Authorized Vehicles List.")

def main():
    while True:
        print("********************************")
        print("AutoCountry Vehicle Finder v0.5")
        print("********************************")
        print("Please Select the following number below from the following menu:")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. DELETE Authorized Vehicle")
        print("5. Exit")
        print("********************************")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print_vehicles()
        elif choice == "2":
            search_vehicle()
        elif choice == "3":
            add_vehicle()
        elif choice == "4":
            delete_vehicle()
        elif choice == "5":
            print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("\nPlease select one of the given options.")

        input("\nPress any key to continue...")

main()
