# Kirill M7P4 09/24/2026

# Start count of total gross and number of employess
total_gross = 0
employees = 0

# Asking user to continue program  
choose_user = str(input("What do you want to continue this program (Y): "))

# Begining of the while loop
while choose_user == "Y":

# Entering employee last name, hours of worked, rate of pay    
    employee_name = input("Enter employee last name of the: ")
    hours_worked = int(input("Enter number of hours worked: "))
    rate_pay = int(input("Enter rate of pay: "))

# If statement: hours is less than 40, add overtime pay, else hours of worked by rate of pay 
    if hours_worked > 40:
        regular_pay = 40 * rate_pay
        over_time = (hours_worked - 40) * (rate_pay * 1.5)
        gross_pay = regular_pay + over_time
    else:
        gross_pay = hours_worked * rate_pay

# Additing to total gross a gross pay, and for employees one user 
    total_gross += gross_pay
    employees += 1

# Asking user to continue program
    choose_user = str(input("What do you want to continue this program (Y): "))

# Finding average pay by dividing total gross on number of employees
average_pay = total_gross/employees

#Printing sum of gross income, total number of employees, and average foss pay
print()
print(f"Sum of gross income: ${total_gross:.2f}")
print()
print(f"Total number of employees: {employees}")
print()
print(f"Average gross pay: ${average_pay:.2f}")