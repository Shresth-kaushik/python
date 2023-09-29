students_score = input("Enter the student score").split(",") # split where the , occur 

for i in range(0,len(students_score)):
    students_score[i] = int(students_score[i])
print(students_score)    

print(max(students_score))
print(min(students_score)) # inbuilt function can not be used to find the max and min 

max = 0
for i in students_score:
    if max < i:
        max = i   

print(max)


# range()-> function 
# range(starting index , upto where loop runs , increment/ step size )



