# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Mercedes Gonzalez Gonzalez,9.6.2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    import DataClasses as DC  # data classes
    import ProcessingClasses as PC  # processing classes
    import IOClasses as IO  # presentation classes
else:
    raise Exception("This file was not created to be imported")

# Test Person Class in data module
print("Test Person Class in data module")
objP1 = DC.Person("Bob", "Smith")
objP2 = DC.Person("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
PC.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
lstFileData = PC.FileProcessor.read_data_from_file("PersonData.txt")
lstTable.clear()
for row in lstFileData:
    lstTable.append(DC.Person(row[0], row[1].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

# Test Employee Class in data module
print()
print("Test Employee Class in data module")
objE1 = DC.Employee(1, "Bob", "Smith")
objE2 = DC.Employee(2, "Sue", "Jones")
lstTable = [objE1, objE2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
PC.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = PC.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(DC.Employee(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

# Test IO classes
print()
print("Test IO class")
IO.EmployeeIO.print_menu_items()
IO.EmployeeIO.print_current_list_items(lstTable)
print(IO.EmployeeIO.input_employee_data())
print(IO.EmployeeIO.input_menu_options())
