# WAP to get the sum of even numbers from 1 to 100
# Method 1 
sum = 0
for i in range(2,101,2):
    sum+=i
print(sum)    


# Method 2 
total = 0
for i in range(1,101):
    if i%2==0:
        total+=i
print(total)        