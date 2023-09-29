import random

# Data structure to store data -> Multiple data at once 

# fruits = ["Banana","Apple" , "Orange"]

# fruits.append("Pear") # add element to the end of the list 

# fruits.extend(["Grapes" , "Pomeagrant" ,"Blackberry"]) # add a list of items to the end of the list
#  google the other methods . 
# print(fruits)




# Example: Bill payment by random person after dinner at hotel . 


name_string = input("Enter the names separated with commas ")
name = name_string.split(",") # used to sepaeted the name 

num_item = len(name)
random_choice  = random.randint(0, num_item-1)

person_pay_bill = name[random_choice]

# person_pay_bill = random.choice(name) 
# Choice function is used to choose among certain elements .

print(person_pay_bill + " Is going to pay bill for all ")





