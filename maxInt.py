x = int(input("Please enter an int: "))
y = int(input("Please enter an int: "))
z = int(input("Please enter an int: "))
if y > x:
    if z > y:
        print(z, "is the greatest.")

    else:
        print(y, "is the greatest.")

else:
    if z > x:
        print(z, "is the greatest.")

    else:
        print(x, "is the greatest.")
print("Done.")

