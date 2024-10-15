# multiplication table


n = int(input("Enter n: "))
x = int(input("Enter the last number you want to: "))

for i in range(1, x+1):
    print(f"{n} x {i} = {n*i}")


# multiplication table in reverse form


nn = int(input("Enter n: "))
xy = int(input("Enter the last number you want to: "))

for ii in range(1, xy+1):
    print(f"{nn} x {(xy+1)-ii} = {nn*((xy+1)-ii)}")








