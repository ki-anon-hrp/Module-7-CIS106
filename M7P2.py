# Kirill M7P2 09/24/2026

# Entering start, stop, and increment values
start_value = int(input("Enter start value: "))
stop_value = int(input("Enter stop value: "))
increment_value = int(input("Enter increment value: "))

# While loop where start value is initial process, printing it and adding increment value
while start_value <= stop_value:
    print(start_value)
    start_value += increment_value