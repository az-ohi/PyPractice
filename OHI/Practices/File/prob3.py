
with open("my.txt", "r") as f:
    content = f.read()

if ("python" in content):
    print("Python is present")
else:
    print("Python is not present")

# print line number

with open("my.txt", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if ("python" in line):
        print(f"Python is present in line: {lineno}")
        break
    lineno += 1
else:
        print("Python is not present")




















