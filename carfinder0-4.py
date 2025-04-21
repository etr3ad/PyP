# CarFinder - AutoCountry Vehicle Finder v0.4

# List of allowed vehicles
AllowedVehiclesList = [
    'Ford F-150',
    'Chevrolet Silverado',
    'Tesla CyberTruck',
    'Toyota Tundra',
    'Nissan Titan',
    'Rivian R1T',
    'Ram 1500'
]

def display_menu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.4")
    print("********************************")
    print("Please Select the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for vehicle in AllowedVehiclesList:
            print(vehicle)

    elif choice == "2":
        search = input("\nPlease Enter the full Vehicle name: ")
        if search in AllowedVehiclesList:
            print(f"\n'{search}' is an authorized vehicle!")
        else:
            print(f"\n'{search}' is not an authorized vehicle. If you received this in error, please check the spelling and try again.")

    elif choice == "3":
        new_vehicle = input("\nPlease Enter the full Vehicle name you would like to add: ")
        AllowedVehiclesList.append(new_vehicle)
        print(f"\nYou have added '{new_vehicle}' as an authorized vehicle.")

    elif choice == "4":
        remove_vehicle = input("\nPlease Enter the full Vehicle name you would like to REMOVE: ")
        if remove_vehicle in AllowedVehiclesList:
            confirm = input(f"\nAre you sure you want to remove '{remove_vehicle}' from the Authorized Vehicles List? (yes/no): ").lower()
            if confirm == "yes":
                AllowedVehiclesList.remove(remove_vehicle)
                print(f"\nYou have REMOVED '{remove_vehicle}' as an authorized vehicle.")
            else:
                print("\nVehicle not removed.")
        else:
            print(f"\n'{remove_vehicle}' is not in the Authorized Vehicles List.")

    elif choice == "5":
        print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
        break

    else:
        print("\nPlease select one of the given options.")

    input("\nPress Enter to return to the main menu...")
