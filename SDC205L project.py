Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("micwin2135")

from datetime import datetime

student_id = "micwin2135"

print(f"{student_id} Spreadsheet Automation Menu")

menu_options = [
    "1. Input Data",
    "2. Create New Spreadsheet",
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
        return (value - 32) * 5/9  
    elif conversion_type == "lbs to kg":
        return value / 2.205  
    elif conversion_type == "in to cm":
        return value * 2.54  
    else:
        return None
def getInput():
    """Gets user input, processes it, and converts the values."""
    num_entries = int(input("How many entries would you like to input? "))
    for _ in range(num_entries):
        
        date = input("Enter the date (YYYY-MM-DD): ")
        value = float(input("Enter the value (numerical value): "))
        conversion_type = input("Enter the type of conversion (F to C, lbs to kg, in to cm): ")
        converted_value = convertData(value, conversion_type)
        if converted_value is not None:
            print(f"The following was saved at {datetime.now()}:")
            print(f"Date: {date}, Original Value: {value}, Converted Value: {converted_value}")
        else:
            print("Error: Invalid conversion type entered.")

if choice == "1":
    getInput()  
elif choice in ["2", "3", "4"]:
    print(f"You selected option {choice}. The time and date is {current_time}.")
else:
    print("Error: Invalid choice selected.")
