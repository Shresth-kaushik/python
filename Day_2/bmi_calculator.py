# bmi = Weight(kg) / (height^2(meter)) -> formula 
# We have to print the bmi in whole number form 
height = input("Enter the height")
weight = input("Enter the weight") 

type(height) # string type                 
type(weight) #string type 

# conversion to int and flaot 
bmi = int(weight) / (float(height)**2)
print(int(bmi))


# f string concept 

