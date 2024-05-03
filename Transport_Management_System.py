class TransportManagementSystem:
    
    def __init__(self):
        self.vehicles = {}
        self.routes = {}
        self.drivers = {}

    def add_vehicle(self, vehicle_no, vehicle_type):
        if vehicle_no.strip() == '' or vehicle_type.strip() == '':
            print("\n--Vehicle number and type cannot be empty!--\n")
            return
        if vehicle_no in self.vehicles:
            print("\n--Vehicle already exists!--\n")
            return
        self.vehicles[vehicle_no] = vehicle_type
        print("\n--Vehicle added successfully!--\n")

    def add_route(self, route_name, route_details):
        if route_name.strip() == '' or route_details.strip() == '':
            print("\n--Route name and details cannot be empty!--\n")
            return
        if route_name in self.routes:
            print("\n--Route already exists!--\n")
            return
        self.routes[route_name] = route_details
        print("\n--Route added successfully!--\n")

    def add_driver(self, driver_name, contact_no):
        if driver_name.strip() == '' or not contact_no.isdigit() or len(contact_no) != 10:
            print("\n--Invalid driver name or contact number!--\n")
            return
        if driver_name in self.drivers:
            print("\n--Driver already exists!--\n")
            return
        self.drivers[driver_name] = contact_no
        print("\n--Driver added successfully!--\n")

    def delete_vehicle(self, vehicle_no):
        if vehicle_no.strip() == '':
            print("\n--Vehicle number cannot be empty!--\n")
            return
        if vehicle_no not in self.vehicles:
            print("\n--Vehicle not found!--\n")
            return
        self.vehicles.pop(vehicle_no)
        print("\n--Vehicle deleted successfully!--\n")

    def delete_route(self, route_name):
        if route_name.strip() == '':
            print("\n--Route name cannot be empty!--\n")
            return
        if route_name not in self.routes:
            print("\n--Route not found!--\n")
            return
        self.routes.pop(route_name)
        print("\n--Route deleted successfully!--\n")

    def delete_driver(self, driver_name):
        if driver_name.strip() == '':
            print("\n--Driver name cannot be empty!--\n")
            return
        if driver_name not in self.drivers:
            print("\n--Driver not found!--\n")
            return
        self.drivers.pop(driver_name)
        print("\n--Driver deleted successfully!--\n")

    def search_vehicle(self, vehicle_no):
        if vehicle_no.strip() == '':
            print("\n--Vehicle number cannot be empty!--\n")
            return
        if vehicle_no in self.vehicles:
            print(f"{vehicle_no} is in vehicles list.")
        else:
            print(f"{vehicle_no} not in vehicles list.")

    def search_route(self, route_name):
        if route_name.strip() == '':
            print("\n--Route name cannot be empty!--\n")
            return
        if route_name in self.routes:
            print(f"{route_name} is in routes list.")
        else:
            print(f"{route_name} not in routes list.")

    def search_driver(self, driver_name):
        if driver_name.strip() == '':
            print("\n--Driver name cannot be empty!--\n")
            return
        if driver_name in self.drivers:
            print(f"{driver_name} is in drivers list.")
        else:
            print(f"{driver_name} is not in drivers list.")

    def display_vehicles(self):
        print("\n--- List of Vehicles ---\n")
        for vehicle, vehicle_type in self.vehicles.items():
            print(f"{vehicle} : {vehicle_type}")

    def display_routes(self):
        print("\n--- List of Routes ---\n")
        for route, timings in self.routes.items():
            print(f"{route} : {timings}")

    def display_drivers(self):
        print("\n--- List of Drivers ---\n")
        for driver, contact in self.drivers.items():
            print(f"{driver} : {contact}")


if __name__ == "__main__":
    
    transport_system = TransportManagementSystem()
    
    while True:
        print("\nOperations To Perform:-")
        print('''
              1. Add Vehicle
              2. Add Route
              3. Add Driver
              4. Delete Vehicle
              5. Delete Route
              6. Delete Driver
              7. Search Vehicle
              8. Search Route 
              9. Search Driver
              10. Display Vehicles
              11. Display Routes
              12. Display Drivers
              13. Exit''')

        choice = input("\nEnter your choice: ")

        if choice == '1':
            vehicle_no = input("Enter the Reg. no. of vehicle: ")
            vehicle_type = input("Enter the type of vehicle: ")
            transport_system.add_vehicle(vehicle_no, vehicle_type)

        elif choice == '2':
            route_name = input("Enter route name: ")
            route_timings = input("Enter route timings: ")
            transport_system.add_route(route_name, route_timings)

        elif choice == '3':
            driver_name = input("Enter driver name: ")
            contact_no = input("Enter Phone no: ")
            transport_system.add_driver(driver_name, contact_no)

        elif choice == '4':
            vehicle_no = input("Enter Vehicle no. : ")
            transport_system.delete_vehicle(vehicle_no)

        elif choice == '5':
            route_name = input("Enter route name: ")
            transport_system.delete_route(route_name)

        elif choice == '6':
            driver_name = input("Enter the name of driver: ")
            transport_system.delete_driver(driver_name)

        elif choice == '7':
            v_no = input("Enter the vehicle no. you want to search: ")
            transport_system.search_vehicle(v_no)

        elif choice == '8':
            name = input("Enter the route name you want to search: ")
            transport_system.search_route(name)

        elif choice == '9':
            dri_name = input("Enter the name of driver you want to search: ")
            transport_system.search_driver(dri_name)

        elif choice == '10':
            transport_system.display_vehicles()

        elif choice == '11':
            transport_system.display_routes()

        elif choice == '12':
            transport_system.display_drivers()

        elif choice == '13':
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.\n")
