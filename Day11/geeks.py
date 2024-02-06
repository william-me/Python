file = open("geeks.txt", 'r')
for x in file:
    print(x)

file = open("geeks.txt", "r")
print(file.read())

with open("geeks.txt") as file:
    data = file.read()
print(data)

#read the fisrt 5 characters
file = open("geeks.txt", "r")
print(file.read(5))

#split
with open("geeks.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

#create a file
file = open("new.txt", "w")
file.write("This is file operations.")
file.write("It allows us to write a particular file")
file.close()

#write a particular file
with open("geeks.txt", "w") as f:
    f.write("Hi there!\n")

#Append mode
file = open("geeks.txt", "a")
file.write("Its a new line")
file.close()