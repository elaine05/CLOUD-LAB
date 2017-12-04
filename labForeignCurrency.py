amt = float(input("What is the amount of US Dollars you wish to convert?"))
rate = float(input("What is the current exchange rate ( 1USD equals what in Foreign Currency)?"))
res = amt * rate
print("The amount in the foreign currency is " + str(round(res,2)))
