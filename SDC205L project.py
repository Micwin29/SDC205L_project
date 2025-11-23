Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

from datetime import datetime

student_id = "micwin2135"

# Display the application's name
print(f"{student_id} Spreadsheet Automation Menu")

# Menu options stored in a list
menu_options = [
    "1. Open Spreadsheet",
    "2. Create New Spreadsheet",
    "3. Edit Spreadsheet",
    "4. Exit"
]

# Loop through and print each menu option
for option in menu_options:
    print(option)


choice = input("Please select an option by entering the corresponding number: ")


current_time = str(datetime.now())


if choice in ["1", "2", "3", "4"]:
    print(f"You selected option {choice}. The time and date is {current_time}.")
else:
    print("Error: Invalid choice selected.")
