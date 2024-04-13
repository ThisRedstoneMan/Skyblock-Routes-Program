import os
import pyperclip

routes_folder = 'routes'

def list_files_in_routes_folder():
    print("List of files in the 'routes' folder:")
    files = os.listdir(routes_folder)
    for file in files:
        print(file)

while True:
    print('Press 1 to read a route, 2 to save a route, 3 to delete a route, and 4 to exit:')
    choice = input()

    if choice == '1':
        list_files_in_routes_folder()
        print('Enter the name of the route you wanna copy:')
        route_to_copy = input()
        file_path = os.path.join(routes_folder, route_to_copy + '.route')
        # Check if the file exists
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                route_contents = file.read()
                # Copy contents to clipboard
                pyperclip.copy(route_contents)
                print(f"Contents of '{route_to_copy}' copied to clipboard.")
        else:
            print(f"Route '{route_to_copy}' does not exist.")

    elif choice == '2':
        print('Type the name of the route:')
        routeName = input()
        print('Type the Route:')
        routeString = input()
        # Check if the 'routes' folder exists, if not, create it
        if not os.path.exists(routes_folder):
            os.makedirs(routes_folder)
        # Specify the path to the 'routes' folder when saving the file
        with open(os.path.join(routes_folder, routeName + '.route'), "x") as file:
            file.write(routeString)
        print("Choice 2")

    elif choice == "3":
        list_files_in_routes_folder()
        print("Enter the name of the route you wanna delete:")
        file_to_delete = input()
        file_path = os.path.join(routes_folder, file_to_delete + '.route')
        # Check if the file exists
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Route '{file_to_delete}' has been deleted.")
        else:
            print(f"Route '{file_to_delete}' does not exist.")

    elif choice == "4":
        print("Exiting...")
        break  # Exit the loop and end the program

    else:
        print("Invalid choice. Please select a valid option.")
