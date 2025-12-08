Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("micwin2135")

from datetime import datetime
import os

student_id = "micwin2135"
print(f"{student_id} Spreadsheet Automation Menu")

menu_options = [
    "1. Input Data",
    "2. View Spreadsheet Data",
    "3. Edit Spreadsheet",
    "4. Exit"
]

for option in menu_options:
    print(option)

choice = input("Please select an option by entering the corresponding number: ")
current_time = str(datetime.now())

def convertData(value, conversion_type):
    """Converts the given value based on the conversion type."""
    if conversion_type == "F to C":
        return (value - 32) * 5 / 9
    elif conversion_type == "lbs to kg":
        return value / 2.205
    elif conversion_type == "in to cm":
        return value * 2.54
    else:
        return None

def insertData(path, data):
    """Appends comma-separated data to the CSV file, creating it if needed."""
    try:
        with open(path, "a") as file:  # minimal permissions for append
            file.write(data + "\n")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

def viewData(path):
    """Reads and prints the contents of the CSV file."""
    try:
        with open(path, "r") as file:
            print(f"\n--- Displaying contents of {path} ---\n")
            print(file.read())
    except Exception as e:
        print(f"Error reading file: {e}")

def getInput():
    """Gets user input, converts values, and saves them to ZooData.csv."""
    csv_path = "ZooData.csv"

    try:
        num_entries = int(input("How many entries would you like to input? "))
    except ValueError:
        print("Error: You must enter a number.")
        return

    for _ in range(num_entries):
        date = input("Enter the date (YYYY-MM-DD): ")
        value = float(input("Enter the value (numerical value): "))
        conversion_type = input("Enter the type of conversion (F to C, lbs to kg, in to cm): ")

        converted_value = convertData(value, conversion_type)

        if converted_value is None:
            print("Error: Invalid conversion type entered.")
            continue

        # build line to write to CSV
        data_line = f"{date},{value},{conversion_type},{converted_value}"

        # Attempt to write using insertData()
        try:
            success = insertData(csv_path, data_line)
            if success:
                print(f"The following data was saved at {datetime.now()}: {data_line}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if choice == "1":
    getInput()

elif choice == "2":
    viewData("ZooData.csv")

elif choice in ["3", "4"]:
    print(f"You selected option {choice}. The time and date is {current_time}.")

else:
    print("Error: Invalid choice selected.")
