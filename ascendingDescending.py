import random
 
print("Generating 100 random numbers....")

arr = [100]
for i in range (100):
    n = [random.randint(1,200)]
    arr = arr + n

print("Ascending:",sorted(arr))
print("Descending:",sorted(arr,reverse=True))

      
