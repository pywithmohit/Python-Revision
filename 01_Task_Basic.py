# Requirements
# Your program must:
# 1. Store the employee's name, employee ID, department, and monthly basic salary in variables.
# 2. Ask the user to enter these details using input().
# 3. Convert the salary into a numeric data type using type casting.
# 4. Calculate the following:
# HRA = 20% of basic salary
# DA = 10% of basic salary
# Bonus = 5% of basic salary
# Gross salary = Basic salary + HRA + DA + Bonus
employee_name = input("Enter Employee_Name : ")
employee_id = input("Enter Employee_id : ")
department = input("Enter Department : ")
Basic_salary = int(input("Enter the salary :"))
HRA = Basic_salary * 0.20
DA = Basic_salary * 0.10
Bonus = Basic_salary * 0.05
Gross_salary = Basic_salary + HRA + DA + Bonus
print(f"employee_name--> {employee_name}")
print(f"employee_id--> {employee_id}")
print(f"department--> {department}")
print(f"Gross_salary--> {Gross_salary}")