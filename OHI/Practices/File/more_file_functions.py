f = open("myfile.txt")

lines = f.readlines()

print(lines, type(lines))

f.close()

# for line by line

f = open("myfile.txt")

line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))

line5 = f.readline()
print(line5, type(line5))

line6 = f.readline()
print(line6,type(line6))

f.close()

# Using while loop

f = open("myfile.txt")

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()

















