# CarFinder - AutoCountry Vehicle Finder v0.1

# List of allowed vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

print("AutoCountry Vehicle Finder v0.1")
print("Please Select the following number below from the following menu:")
print("1. PRINT all Authorized Vehicles")
print("2. Exit")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    print(AllowedVehiclesList[0])
    print(AllowedVehiclesList[1])
    print(AllowedVehiclesList[2])
    print(AllowedVehiclesList[3])
    print(AllowedVehiclesList[4])
elif choice == "2":
    print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
else:
    print("\nplease select one of the given options.")

input("\nPress Enter to close the program...")
