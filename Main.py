# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Mercedes Gonzalez Gonzalez,9.6.2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #

import DataClasses as DC  # data classes
import ProcessingClasses as PC  # processing classes
import IOClasses as IO  # presentation classes


def main():
    file_name = 'EmployeeData.txt'
    employee_list = []

    # Load data from file into a list of employee objects when script starts
    file_data = PC.FileProcessor.read_data_from_file(file_name)
    for line in file_data:
        employee_list.append(DC.Employee(line[0], line[1], line[2].strip()))

    while True:
        IO.EmployeeIO.print_menu_items()  # Show user a menu of options
        strChoice = IO.EmployeeIO.input_menu_options()  # Get user's menu option choice

        # Process user's menu choice
        if strChoice == '1':  # Show current employee data
            IO.EmployeeIO.print_current_list_items(employee_list)
            continue  # to show the menu

        elif strChoice.strip() == '2':  # Add a new Employee Data
            new_employee = IO.EmployeeIO.input_employee_data()
            employee_list.append(new_employee)
            continue  # to show the menu

        elif strChoice == '3':  # Save employee data to File
            PC.FileProcessor.save_data_to_file(file_name, employee_list)
            continue  # to show the menu

        elif strChoice == '4':  # Exit Program
            print("Goodbye!")
            break  # and Exit


if __name__ == "__main__":
    main()
else:
    raise Exception("This file was not created to be imported")
