# CarFinder - AutoCountry Vehicle Finder v0.3

# List of allowed vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.3")
    print("********************************")
    print("Please Select the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. Exit")
    print("********************************")

while True:
    display_menu()
    choice = input("Enter your choice (1, 2, 3 or 4): ")

    if choice == "1":
        print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for vehicle in AllowedVehiclesList:
            print(vehicle)

    elif choice == "2":
        search = input("\nPlease Enter the full Vehicle name: ")
        if search in AllowedVehiclesList:
            print(f"\nYes, '{search}' is an authorized vehicle!")
        else:
            print(f"\n'{search}' is not an authorized vehicle. If you received this in error, please check the spelling and try again.")

    elif choice == "3":
        new_vehicle = input("\nPlease Enter the full Vehicle name you would like to add: ")
        AllowedVehiclesList.append(new_vehicle)
        print(f'\nYou have added "{new_vehicle}" as an authorized vehicle.')

    elif choice == "4":
        print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
        break

    else:
        print("\nPlease select one of the given options.")

    input("\nPress Enter to return to the main menu...")
