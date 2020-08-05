employee_file = open("employees.txt", "a") # 'a' appends to the file; 'w' overwrites the entire file and can be used to create a new file on the spot

employee_file.write("\nKelly - Customer Service") # Appends to a new file on a new line

employee_file.close()