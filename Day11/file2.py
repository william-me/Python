f = open("demofile.txt", "r")
print(f.read())

f = open("demofile.txt", "r")
print(f.read(6))

f = open("demofile.txt", "r")
print(f.readline())
for x in f:
    print(x)
f.close()

f = open("demofile.txt", "w")
f.write("I have written the file")
f.close()

f = open("demofile.txt", "r")
print(f.read())

#write a new file
f = open("myfile.txt", "w")
print(f.read())

