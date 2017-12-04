x = float(input("Please enter a number: "))
y = float(input("Please enter a number: "))

print("1) Add the two numbers")

print("2) Subtract the two numbers")

print("3) Multiply the two numbers")

print("4) Divide the two numbers")

ch = int(input("Please enter your choice: "))

print("The answer is: ", end = ".")

if ch ==1:
    print(x+y)

else:
    if ch == 2:
        print(x-y)

    else:
        if ch == 3:
            print(x*y)

        else:
            if ch == 4:
                print(x/y)
            else:
                print("You did not enter a valid choice")

                
