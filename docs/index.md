# Introduction 

This week, as part of Module 9 in Foundation of Programming (Python) course, I learned how to work with modules and classes in Python. The lesson was focused on how to organize code into classes, which reside in different modules, used as libraries and then import those library modules into the main application module, which is invoked from the command line. As part of this assignment, I combined the knowledge I learned in the course about modules, classes, constructors, properties, methods, data serialization and exception handling to create a script that interacts with users to create, display and save a list of employees. This document contains a step-by-step description on how the script was created and tested.

## The TestHarness Module
The TestHarness module main objective was to test the Data, Processing and Presentation layer classes. At the start of the module, there are “import” directives to load the DataClasses, ProcessingClasses and IOClasses modules. The DataClasses module contains the Person Class and the Employee Class, which inherits from the Person Class. Both classes were tested along with the FileProcessor class contained within the ProcessingClasses module. The tests consisted on using a workflow that:
*	  Created two object instances from each class
*		Printed their string representation in console along with their class type
*		Saved the objects into a file
*		Reloaded the objects from the file into a list of string data
*		Turned that list of string data into a list of objects from the original class. 
Note: The code pertaining to the DataClasses, ProcessingClasses and IOClasses is not listed in this document, because it was already discussed during the lesson, but I included it in the repository files

![TestHarness module code](https://github.com/mglezglez/IntroToProg-Python-Mod09/blob/master/docs/TestHarness.py.PNG "TestHarness module code")

## Running the TestHarness Module
In order to test that the TestHarness module worked as expected, it ran and I was able to confirm that the desired output was obtained while testing it. Figure 2 contains the output of running the module in PyCharm.

![Testing the TestHarness module](https://github.com/mglezglez/IntroToProg-Python-Mod09/blob/master/docs/TestHarness.PNG "Testing the TestHarness module")

## The Main Module
Once the TestHarness module proved that the basic functionality included in each class worked as expected, I proceeded to work on the Main module. The Main module combined the three classes for Data (DataClasses), Processing (ProcessingClasses) and Presentation (IOClasses). The main goal of the Main module was to:
*	Load data from a file containing a list of employees
*	Present a menu of options to the user
*	Process the user’s choice in order to: show the current list of employees, allow the user to add a new employee, save the list of employees to a file and exit the main program.

![Main module code](https://github.com/mglezglez/IntroToProg-Python-Mod09/blob/master/docs/MainModule.PNG "Main module code")

## Testing the Main Module
In order to test the Main Module, I conducted two tests:

### Test # 1: Adding new employees and showing the updated list of employees after each addition

### Test # 2: Saving the list of employees to a file

These are screenshots containing the results of each test:

### Test # 1:

![Inserting First Employee](https://github.com/mglezglez/IntroToProg-Python-Mod09/blob/master/docs/InsertingFirstEmployee.PNG "Inserting First Employee")
![Inserting Second Employee](https://github.com/mglezglez/IntroToProg-Python-Mod09/blob/master/docs/InsertingSecondEmployee.PNG "Inserting Second Employee")

### Test # 2:

![Saving Employees Data To File](https://github.com/mglezglez/IntroToProg-Python-Mod09/blob/master/docs/SavingDataToFile.PNG "Saving Employees Data To File")

## Summary
This section of the course introduced the concepts of class inheritance and modules in Python. As we continue to expand our knowledge about this programming language, I found these new features to be very useful in order to improve code reuse and optimization.
