#break statement
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 6:
        break
    print(number)

#continue statement
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 6:
        continue
    print(number)

#loops in Log file analysis   
log_file = [
    "INFO: Successfull",
    "ERROR: File not found",
    "DEBUG: Opening file",
    "ERROR: Database connection failed"
]
for log in log_file:
    if "ERROR" in log:
        print(log)