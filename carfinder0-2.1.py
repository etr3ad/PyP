# CarFinder - AutoCountry Vehicle Finder v0.2

# List of allowed vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

print("********************************")
print("AutoCountry Vehicle Finder v0.2")
print("********************************")
print("Please Select the following number below from the following menu:")
print("1. PRINT all Authorized Vehicles")
print("2. SEARCH for Authorized Vehicle")
print("3. Exit")

choice = input("Enter your choice (1, 2 or 3): ")

if choice == "1":
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    print(AllowedVehiclesList[0])
    print(AllowedVehiclesList[1])
    print(AllowedVehiclesList[2])
    print(AllowedVehiclesList[3])
    print(AllowedVehiclesList[4])

elif choice == "2":
    search = input("\nPlease Enter the full Vehicle name: ")
    if search in AllowedVehiclesList:
        print(f"\n '{search}' is an authorized vehicle!")
    else:
        print(f"\n'{search}' is not an authorized vehicle. If you received this in error, please check the spelling and try again.")

elif choice == "3":
    print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")

else:
    print("\nPlease select one of the given options.")

input("\nPress Enter to close the program...")
