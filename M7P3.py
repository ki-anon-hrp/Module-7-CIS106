# Kirill M7P3 09/24/2026

# Start count of users
user = 0 

# Asking user to continue program
choose_user = str(input("What do you want to continue this program (Y): "))

# Begining of the while loop
while choose_user == "Y":

# Entereing last name, first exam, and second exam score
    last_name = input("Enter your last name: ")
    first_exam = int(input("Enter your first exam score: "))
    second_exam = int(input("Enter your second exam score: "))

# Finding average from two exam
    average_score = (first_exam + second_exam) / 2
    print(f"{last_name}")
    print(f"Your average for two exams: {average_score:.2f}")

# Additing to user variable one user
    user += 1

# Asking user to continue program
    choose_user = str(input("What do you want to continue this program (Y): "))

# Printing final message and number users
print(f"Program is done. Total number of students: {user}")