# Assignment 5: Software-Engineering-Testing

For this assignment you will be tasked with testing the grading system. This system was designed to be a simple version 
of the grading system you have worked on for the past assignments. 


This program contains the following classes:
- System
- User
- Staff
- Student
- TA
- Professor

## Files

### Data
There are two json files with all the user and course information. This information would typically be stored in an actual
database but were stored in "Data/users.json" and "Data/courses.json" to help simplify this assignment.

### System
This is the main class which is used to manage the entire software. Below this class has "if '__name__' == '__main__':" statement 
which contains the first lines run in a python program.

System manages and creates the different users within the system.

### User

This class contains the functions used by all other classes. Staff, and Student both directly inherit the functions in this class.

### Staff

This class contains the functions used by both Professor and TA.

### Student
Student inherits users and contains the functions relevant to the activities the students can perform.

### TA
TA inherits Staff and contains all the relevant functions that the TA can perform.

### Professor
Professor inherits Staff and contains all functions relevant to acitvities the professor can perform.

## Assignment

For this assignment you will need to use Pytest to write tests for the software we have provided. You will need to have 10 total tests and I should be able to run them on my system. Here are the following functions you will need to test:

1. login - System.py
2. check_password - System.py
3. change_grade - TA.py
4. submit_assignment - Student.py
5. check_ontime - Student.py
