employee_file = open("employees.txt", "r")

#print(employee_file.readable()) # makes sure the file opened is readable
#print(employee_file.readline()) # reads the first line and moves the cursor to the next line
#print(employee_file.readline())

#print(employee_file.readlines()) # turns remaining content in file into an array

for employee in employee_file.readlines():
    print(employee)

employee_file.close() #all open files must also be closed