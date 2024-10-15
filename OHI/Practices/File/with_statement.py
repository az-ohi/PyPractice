f = open("file.txt")
print(f.read())
f.close()

# the same can be written using "with" statement

with open("file.txt") as f:
    print(f.read())

# close argument not need to be written










