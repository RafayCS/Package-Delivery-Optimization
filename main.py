import datetime
import truck
from hash_table import ChainingHashTable
from package import Package

# Package data from Package File.csv
package_data = [
    (1, "195 W Oakland Ave", "Salt Lake City", "UT", "84115", "10:30 AM", 21),
    (2, "2530 S 500 E", "Salt Lake City", "UT", "84106", "EOD", 44),
    (3, "233 Canyon Rd", "Salt Lake City", "UT", "84103", "EOD", 2, "Can only be on truck 2"),
    (4, "380 W 2880 S", "Salt Lake City", "UT", "84115", "EOD", 4),
    (5, "410 S State St", "Salt Lake City", "UT", "84111", "EOD", 5),
    (6, "3060 Lester St", "West Valley City", "UT", "84119", "10:30 AM", 88, "Delayed on flight---will not arrive to depot until 9:05 am"),
    (7, "1330 2100 S", "Salt Lake City", "UT", "84106", "EOD", 8),
    (8, "300 State St", "Salt Lake City", "UT", "84103", "EOD", 9),
    (9, "300 State St", "Salt Lake City", "UT", "84103", "EOD", 2, "Wrong address listed"),
    (10, "600 E 900 South", "Salt Lake City", "UT", "84105", "EOD", 1),
    (11, "2600 Taylorsville Blvd", "Salt Lake City", "UT", "84118", "EOD", 1),
    (12, "3575 W Valley Central Station bus Loop", "West Valley City", "UT", "84119", "EOD", 1),
    (13, "2010 W 500 S", "Salt Lake City", "UT", "84104", "10:30 AM", 2),
    (14, "4300 S 1300 E", "Millcreek", "UT", "84117", "10:30 AM", 88, "Must be delivered with 15, 19"),
    (15, "4580 S 2300 E", "Holladay", "UT", "84117", "9:00 AM", 4),
    (16, "4580 S 2300 E", "Holladay", "UT", "84117", "10:30 AM", 88, "Must be delivered with 13, 19"),
    (17, "3148 S 1100 W", "Salt Lake City", "UT", "84119", "EOD", 2),
    (18, "1488 4800 S", "Salt Lake City", "UT", "84123", "EOD", 6, "Can only be on truck 2"),
    (19, "177 W Price Ave", "Salt Lake City", "UT", "84115", "EOD", 37),
    (20, "3595 Main St", "Salt Lake City", "UT", "84115", "10:30 AM", 37, "Must be delivered with 13, 15"),
    (21, "3595 Main St", "Salt Lake City", "UT", "84115", "EOD", 3),
    (22, "6351 South 900 East", "Murray", "UT", "84121", "EOD", 2),
    (23, "5100 South 2700 West", "Salt Lake City", "UT", "84118", "EOD", 5),
    (24, "5025 State St", "Murray", "UT", "84107", "EOD", 7),
    (25, "5383 South 900 East #104", "Salt Lake City", "UT", "84117", "10:30 AM", 7, "Delayed on flight---will not arrive to depot until 9:05 am"),
    (26, "5383 South 900 East #104", "Salt Lake City", "UT", "84117", "EOD", 25),
    (27, "1060 Dalton Ave S", "Salt Lake City", "UT", "84104", "EOD", 5),
    (28, "2835 Main St", "Salt Lake City", "UT", "84115", "EOD", 7, "Delayed on flight---will not arrive to depot until 9:05 am"),
    (29, "1330 2100 S", "Salt Lake City", "UT", "84106", "10:30 AM", 2),
    (30, "300 State St", "Salt Lake City", "UT", "84103", "10:30 AM", 1),
    (31, "3365 S 900 W", "Salt Lake City", "UT", "84119", "10:30 AM", 1),
    (32, "3365 S 900 W", "Salt Lake City", "UT", "84119", "EOD", 1, "Delayed on flight---will not arrive to depot until 9:05 am"),
    (33, "2530 S 500 E", "Salt Lake City", "UT", "84106", "EOD", 1),
    (34, "4580 S 2300 E", "Holladay", "UT", "84117", "10:30 AM", 2),
    (35, "1060 Dalton Ave S", "Salt Lake City", "UT", "84104", "EOD", 88),
    (36, "2300 Parkway Blvd", "West Valley City", "UT", "84119", "EOD", 88, "Can only be on truck 2"),
    (37, "410 S State St", "Salt Lake City", "UT", "84111", "10:30 AM", 2),
    (38, "410 S State St", "Salt Lake City", "UT", "84111", "EOD", 9, "Can only be on truck 2"),
    (39, "2010 W 500 S", "Salt Lake City", "UT", "84104", "EOD", 9),
    (40, "380 W 2880 S", "Salt Lake City", "UT", "84115", "10:30 AM", 45),
]


def load_package_data(package_hash_table): # Loading package data function with a parameter

    for data in package_data:

        p_id, p_address, p_city, p_state, p_zip_code, p_delivery_deadline, p_weight, *note = data
        p_status = "Package at hub"
        p_note = note[0] if note else None

        # Creates a new instance of the Package class "p" using the extracted data
        package = Package(p_id,p_address,p_city,p_state,p_zip_code,p_delivery_deadline,p_weight,p_status)

        # Inserts the Package object "package" into the hash table, using the package ID "p_id" as the key
        # This makes the package retrievable from the hash table by its ID.
        package_hash_table.insert(p_id, package)

# Address list
address_list = [
    "4001 south 700 east",
    "1060 dalton ave s",
    "1330 2100 s",
    "1488 4800 s",
    "177 w price ave",
    "195 w oakland ave",
    "2010 w 500 s",
    "2300 parkway blvd",
    "233 canyon rd",
    "2530 s 500 e",
    "2600 taylorsville blvd",
    "2835 main st",
    "300 state st",
    "3060 lester st",
    "3148 s 1100 w",
    "3365 s 900 w",
    "3575 w valley central station bus loop",
    "3595 main st",
    "380 w 2880 s",
    "410 s state st",
    "4300 s 1300 e",
    "4580 s 2300 e",
    "5025 state st",
    "5100 south 2700 west",
    "5383 south 900 east #104",
    "600 e 900 south",
    "6351 south 900 east"
]

# Distance matrix
distance_data = [
    ["0.0", "7.2", "3.8", "11.0", "2.2", "3.5", "10.9", "8.6", "7.6", "2.8", "6.4", "3.2", "7.6", "5.2", "4.4", "3.7", "7.6", "2.0", "3.6", "6.5", "1.9", "3.4", "2.4", "6.4", "2.4", "5.0", "3.6"],
    ["7.2", "0.0", "7.1", "6.4", "6.0", "4.8", "1.6", "2.8", "4.8", "6.3", "7.3", "5.3", "4.8", "3.0", "4.6", "4.5", "7.4", "6.0", "5.0", "4.8", "9.5", "10.9", "8.3", "6.9", "10.0", "4.4", "13.0"],
    ["3.8", "7.1", "0.0", "9.2", "4.4", "2.8", "8.6", "6.3", "5.3", "1.6", "10.4", "3.0", "5.3", "6.5", "5.6", "5.8", "5.7", "4.1", "3.6", "4.3", "3.3", "5.0", "6.1", "9.7", "6.1", "2.8", "7.4"],
    ["11.0", "6.4", "9.2", "0.0", "5.6", "6.9", "8.6", "4.0", "11.1", "7.3", "1.0", "6.4", "11.1", "3.9", "4.3", "4.4", "7.2", "5.3", "6.0", "10.6", "5.9", "7.4", "4.7", "0.6", "6.4", "10.1", "10.1"],
    ["2.2", "6.0", "4.4", "5.6", "0.0", "1.9", "7.9", "5.1", "7.5", "2.6", "6.5", "1.5", "7.5", "3.2", "2.4", "2.7", "1.4", "0.5", "1.7", "6.5", "3.2", "5.2", "2.5", "6.0", "4.2", "5.4", "5.5"],
    ["3.5", "4.8", "2.8", "6.9", "1.9", "0.0", "6.3", "4.3", "4.5", "1.5", "8.7", "0.8", "4.5", "3.9", "3.0", "3.8", "5.7", "1.9", "1.1", "3.5", "4.9", "6.9", "4.2", "9.0", "5.9", "3.5", "7.2"],
    ["10.9", "1.6", "8.6", "8.6", "7.9", "6.3", "0.0", "4.0", "4.2", "8.0", "8.6", "6.9", "4.2", "4.2", "8.0", "5.8", "7.2", "7.7", "6.6", "3.2", "11.2", "12.7", "10.0", "8.2", "11.7", "5.1", "14.2"],
    ["8.6", "2.8", "6.3", "4.0", "5.1", "4.3", "4.0", "0.0", "7.7", "9.3", "4.6", "4.8", "7.7", "1.6", "3.3", "3.4", "3.1", "5.1", "4.6", "6.7", "8.1", "10.4", "7.8", "4.2", "9.5", "6.2", "10.7"],
    ["7.6", "4.8", "5.3", "11.1", "7.5", "4.5", "4.2", "7.7", "0.0", "4.8", "11.9", "4.7", "0.6", "7.6", "7.8", "6.6", "7.2", "5.9", "5.4", "1.0", "8.5", "10.3", "7.8", "11.5", "9.5", "2.8", "14.1"],
    ["2.8", "6.3", "1.6", "7.3", "2.6", "1.5", "8.0", "9.3", "4.8", "0.0", "9.4", "1.1", "5.1", "4.6", "3.7", "4.0", "6.1", "2.3", "1.8", "4.1", "3.8", "5.8", "4.3", "7.8", "4.9", "3.2", "6.0"],
    ["6.4", "7.3", "10.4", "1.0", "6.5", "8.7", "8.6", "4.6", "11.9", "9.4", "0.0", "7.3", "12.0", "4.9", "5.2", "5.4", "8.1", "6.2", "6.9", "11.5", "6.9", "7.9", "4.4", "0.4", "5.4", "11.0", "13.6"],
    ["3.2", "5.3", "3.0", "6.4", "1.5", "0.8", "6.9", "4.8", "4.7", "1.1", "7.3", "0.0", "4.7", "3.5", "2.6", "2.9", "6.3", "1.2", "1.0", "3.7", "4.1", "6.2", "3.4", "6.9", "5.2", "3.7", "6.4"],
    ["7.6", "4.8", "5.3", "11.1", "7.5", "4.5", "4.2", "7.7", "0.6", "5.1", "12.0", "4.7", "0.0", "7.3", "7.8", "6.6", "7.2", "5.9", "5.4", "1.0", "8.5", "10.3", "7.8", "11.5", "9.5", "2.8", "14.1"],
    ["5.2", "3.0", "6.5", "3.9", "3.2", "3.9", "4.2", "1.6", "7.6", "4.6", "4.9", "3.5", "7.3", "0.0", "1.3", "1.5", "4.0", "3.2", "3.0", "6.9", "6.2", "8.2", "5.5", "4.4", "7.2", "6.4", "10.5"],
    ["4.4", "4.6", "5.6", "4.3", "2.4", "3.0", "8.0", "3.3", "7.8", "3.7", "5.2", "2.6", "7.8", "1.3", "0.0", "0.6", "4.0", "2.4", "2.2", "6.8", "5.3", "7.4", "4.6", "6.4", "5.4", "4.2", "8.8"],
    ["3.7", "4.5", "5.8", "4.4", "2.7", "3.8", "5.8", "3.4", "6.6", "4.0", "5.4", "2.9", "6.6", "1.5", "0.6", "0.0", "4.6", "3.1", "3.0", "5.7", "6.9", "8.4", "5.4", "4.8", "6.9", "5.7", "8.4"],
    ["7.6", "7.4", "5.7", "7.2", "1.4", "5.7", "7.2", "3.1", "7.2", "6.7", "8.1", "6.3", "7.2", "4.0", "6.4", "5.6", "0.0", "7.1", "6.1", "6.5", "10.6", "12.0", "9.4", "7.5", "11.1", "6.2", "13.6"],
    ["2.0", "6.0", "4.1", "5.3", "0.5", "1.9", "7.7", "5.1", "5.9", "2.3", "6.2", "1.2", "5.9", "3.2", "2.4", "1.6", "7.1", "0.0", "1.6", "4.4", "3.0", "5.0", "3.9", "7.1", "4.0", "5.1", "5.2"],
    ["3.6", "5.0", "3.6", "6.0", "1.7", "1.1", "6.6", "4.6", "5.4", "1.8", "6.9", "1.0", "5.4", "3.0", "2.2", "1.7", "6.1", "1.6", "0.0", "4.6", "4.4", "6.9", "4.6", "7.2", "5.6", "4.3", "6.9"],
    ["6.5", "4.8", "4.3", "10.6", "6.5", "3.5", "3.2", "6.7", "1.0", "4.1", "11.5", "3.7", "1.0", "6.9", "6.8", "6.4", "7.2", "4.9", "4.4", "0.0", "8.5", "10.3", "7.8", "11.5", "9.5", "2.8", "14.1"],
    ["1.9", "9.5", "3.3", "5.9", "3.2", "4.9", "11.2", "8.1", "8.5", "3.8", "6.9", "4.1", "8.5", "6.2", "5.3", "4.9", "10.6", "3.0", "4.6", "7.5", "0.0", "2.0", "2.9", "6.4", "3.5", "6.0", "4.1"],
    ["3.4", "10.9", "5.0", "7.4", "5.2", "6.9", "12.7", "10.4", "10.3", "5.8", "8.3", "6.2", "10.3", "8.2", "7.4", "6.9", "12.0", "5.0", "6.6", "9.3", "2.0", "0.0", "3.4", "7.9", "4.5", "7.6", "4.7"],
    ["2.4", "8.3", "6.1", "4.7", "2.5", "4.2", "10.0", "7.8", "7.8", "4.3", "4.1", "3.4", "7.8", "5.5", "4.6", "4.2", "9.4", "2.3", "3.9", "6.8", "2.9", "3.4", "0.0", "5.4", "2.4", "6.8", "3.1"],
    ["6.4", "6.9", "9.7", "0.6", "6.0", "9.0", "8.2", "4.2", "11.5", "7.8", "0.4", "6.9", "11.5", "4.4", "4.8", "5.6", "7.5", "5.5", "6.5", "11.4", "6.4", "7.9", "5.4", "0.0", "6.4", "10.6", "13.1"],
    ["2.4", "10.0", "6.1", "6.4", "4.2", "5.9", "11.7", "9.5", "9.5", "4.8", "4.9", "5.2", "9.5", "7.2", "6.3", "5.9", "11.1", "4.0", "5.6", "8.5", "3.5", "4.5", "2.4", "6.4", "0.0", "7.0", "1.3"],
    ["5.0", "4.4", "2.8", "10.1", "5.4", "3.5", "5.1", "6.2", "2.8", "3.2", "11.0", "3.7", "2.8", "6.4", "6.5", "5.7", "6.2", "5.1", "4.3", "1.8", "6.0", "7.9", "6.8", "10.6", "7.0", "0.0", "8.3"],
    ["3.6", "13.0", "7.4", "10.1", "5.5", "7.2", "14.2", "10.7", "14.1", "6.0", "6.8", "6.4", "14.1", "10.5", "8.8", "8.4", "13.6", "5.2", "6.9", "13.1", "4.1", "4.7", "3.1", "7.8", "1.3", "8.3", "0.0"]
]

# Function to get the distance between two addresses
def get_distance(address_one, address_two):
    try:
        address_one = address_one.strip().lower()
        address_two = address_two.strip().lower()

        # Ensure both addresses exist in the list
        if address_one not in address_list:
            print(f"Address '{address_one}' not found in address list.")
            return None
        if address_two not in address_list:
            print(f"Address '{address_two}' not found in address list.")
            return None

        # Find indexes and return the distance
        index1 = address_list.index(address_one)
        index2 = address_list.index(address_two)
        distance = distance_data[index1][index2]
        return float(distance)
    except ValueError:
        print(f"One of the addresses '{address_one}' or '{address_two}' not found.")
        return None

def extract_address(address):

    try:
        cleaned_address = address.strip().lower()
        # find and return the index of the address in the address list
        return address_list.index(cleaned_address)
    except ValueError:
        print(f"Address '{address} not found in address list.")
        return None

def correct_package_address(package_hash_table):
    # Update package 9 address to the correct one
    package_nine = package_hash_table.lookup(9)
    if package_nine:
        # correct address
        package_nine.address = '410 S State St'
        package_nine.zip_code = '84111'
        # print('Address for package 9 updated to 410 S State St')

# Instantiating truck one
truck_one = truck.Truck(1,16,0.0,18,None,datetime.timedelta(hours=8),[1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40],'4001 South 700 East')

# Instantiating truck two
truck_two = truck.Truck(2,16,0.0,18,None,datetime.timedelta(hours=10, minutes=20),[3, 9, 12, 17, 18, 22, 23, 24, 26, 27, 35, 36, 38, 39],'4001 South 700 East')

# Instantiating truck three
truck_three = truck.Truck(3,16,0.0,18,None,datetime.timedelta(hours=9, minutes=5),[2, 4, 5, 6, 7, 8, 10, 11, 21, 25, 28, 32, 33],'4001 South 700 East')

# Creating hash table
package_hash_table = ChainingHashTable()

# Loading packages into hash table
load_package_data(package_hash_table)


# Optimizes the delivery route for a truck using the nearest neighbor algorithm.
# Updates the truck's delivery order, mileage, and package delivery times
def optimize_truck_route(truck, package_hash_table):

    # list of packages yet to be delivered
    undelivered_packages = []

    # Retrieve the packages assigned to the truck
    for package_id in truck.packages:
        package = package_hash_table.lookup(package_id)
        if package:
            package.truck_number = truck.number # Assigning truck number
            undelivered_packages.append(package)

    # Clear the truck's package list to prepare for adding packages in the optimized delivery order
    truck.packages.clear()

    # Optimize package delivery order
    while undelivered_packages:
        nearest_package = None
        shortest_distance = float('inf')

        # Find the nearest package to the truck's current location
        for package in undelivered_packages:
            distance_to_package = get_distance(truck.address, package.address)
            if distance_to_package is not None and distance_to_package < shortest_distance:
                shortest_distance = distance_to_package
                nearest_package = package


        if nearest_package:
            # Add the nearest package to the truck's delivery list
            truck.packages.append(nearest_package.ID)

            # Update truck's mileage and location
            truck.mileage = truck.mileage + shortest_distance
            truck.address = nearest_package.address

            # Calculate the time it takes to travel to the next package (truck speed is 18 mph)
            travel_time = datetime.timedelta(hours=shortest_distance / 18)
            truck.time += travel_time
            # Record the time the package was delivered
            nearest_package.delivery_time = truck.time
            # Record the time the package left the hub/ departure time of the truck
            nearest_package.departure_time = truck.depart_time

            # Remove the delivered package from the list
            undelivered_packages.remove(nearest_package)

# Correct package 9's address before truck_two departs
correct_package_address(package_hash_table)

# Optimizing routes for all trucks
optimize_truck_route(truck_one, package_hash_table)
optimize_truck_route(truck_two, package_hash_table)

# Ensuring truck_three waits until truck_one or truck_two returns
truck_three.depart_time = min(truck_one.time, truck_two.time)
optimize_truck_route(truck_three, package_hash_table)

class Main:

    print('Welcome to Parcel Service')
    # Display total mileage of all trucks
    total_mileage = truck_one.mileage + truck_two.mileage + truck_three.mileage
    print(f"Total mileage for all trucks: {total_mileage} miles")

    # Ask the user to type "time" to proceed
    user_input = input("To check package status, type 'time'. To exit, press enter: ").strip().lower()

    if user_input == 'time':
        try:
            # Ask the user to enter a specific time
            user_time_input = input('Enter a time to check package status (HH:MM:SS): ').strip()
            hours, minutes, seconds = map(int, user_time_input.split(':'))
            user_time = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)

            # Ask the user if they want to check a single package or all packages
            package_check_option = input("Type 'solo' to check a single package or 'all' to view all packages: ").strip().lower()

            if package_check_option == 'solo':
                try:
                    # Ask for a specific package ID
                    package_id = int(input('Enter the package ID: ').strip())
                    package = package_hash_table.lookup(package_id)

                    if package:
                        # Update and display the status of the selected package
                        package.update_package_status(user_time)
                        print('Package details: ')
                        print(package)
                    else:
                        print(f"Package ID {package_id} not found.")
                except ValueError:
                    print("Invalid package ID. Please try again.")
            elif package_check_option == 'all':
                print('All package details: ')
                try:
                    # Loop through all packages (assuming IDs are sequential)
                    for package_id in range(1, 41):
                        package = package_hash_table.lookup(package_id)

                        if package:
                            # Update and display the status of each package
                            package.update_package_status(user_time)
                            print(package)
                        else:
                            print(f"Package ID {package_id} not found.")
                except ValueError:
                    print('Error retrieving package data')
            else:
                print('Invalid option. Exiting program.')
        except (ValueError, IndexError):
            print('Invalid time format. Please use HH:MM:SS.')
    else:
        print('Exiting program. Goodbye!')


















































































