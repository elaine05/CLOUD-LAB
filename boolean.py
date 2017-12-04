age = int(input("Please enter your age: "))
mem = True
if age <= 15:
    mem = False
if age >= 18:
    mem = False

if mem:
    print("You can join")
else:
        print("You can't join")
