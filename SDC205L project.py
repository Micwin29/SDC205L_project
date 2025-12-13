Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("micwin2135")

from datetime import datetime
import os
import csv
import openpyxl
from openpyxl.chart import LineChart, BarChart, Reference

student_id = "micwin2135"
print(f"{student_id} Spreadsheet Automation Menu")

menu_options = [
    "1. Input Data",
    "2. View Spreadsheet Data",
    "3. Generate Report",
    "4. Exit"
]

# Display the menu options
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
        with open(path, "a") as file:
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

        data_line = f"{date},{value},{conversion_type},{converted_value}"

        # Attempt to write using insertData()
        try:
            success = insertData(csv_path, data_line)
            if success:
                print(f"The following data was saved at {datetime.now()}: {data_line}")
        except Exception as e:
            print(f"Unexpected error: {e}")

def createChart(path, chart_type):
    """Generates a chart from the CSV data and saves it to an Excel file.
    
    Arguments:
        path (str): The path to the CSV data file.
        chart_type (str): The type of chart to generate ("line" or "bar").
    
    No return value. The chart is saved to 'final.xlsx'.
    """
    try:
        # Read data from the CSV file
        dates = []
        values = []
        converted_values = []

        with open(path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                dates.append(row[0])  # Date in column 1
                values.append(float(row[1]))  # Original value in column 2
                converted_values.append(float(row[3]))  # Converted value in column 4

        # Create a new Excel workbook
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Data"

        # Write the data to the Excel sheet
        for i, date in enumerate(dates):
            ws.append([date, values[i], converted_values[i]])

        # Create the chart
        if chart_type == "line":
            chart = LineChart()
        elif chart_type == "bar":
            chart = BarChart()
        else:
            print("Error: Invalid chart type specified.")
            return

        # Add data to the chart (Converted values as the series, dates as labels)
        data = Reference(ws, min_col=3, min_row=1, max_row=len(dates))
        categories = Reference(ws, min_col=1, min_row=2, max_row=len(dates))

        chart.add_data(data, titles_from_data=True)
        chart.set_categories(categories)

        # Add the chart to the worksheet
        ws.add_chart(chart, "E5")

        # Set the title of the chart to <student_id> <current_date>
        chart.title = f"{student_id} {datetime.now().strftime('%B %d, %Y')}"

        # Save the Excel file
        wb.save("final.xlsx")
        print(f"Chart has been saved to final.xlsx.")

    except Exception as e:
        print(f"Error generating the chart: {e}")

def generateReport(path):
    """Generates a report based on the user's chart type choice.
    
    Arguments:
        path (str): The path to the CSV data file.
    
    Calls createChart and generates either a line or bar chart.
    """
    chart_type = input("Which type of chart would you like to create? (line/bar): ").lower()
    
    # Validate the chart type
    if chart_type not in ['line', 'bar']:
        print("Error: Invalid chart type. Please choose either 'line' or 'bar'.")
        return

    # Call the createChart function to generate and save the chart
    createChart(path, chart_type)

# Main program logic based on user input
if choice == "1":
    getInput()

elif choice == "2":
    viewData("ZooData.csv")

elif choice == "3":
    generateReport("ZooData.csv")

elif choice == "4":
    print(f"You selected option 4. The time and date is {current_time}.")

else:
    print("Error: Invalid choice selected.")
