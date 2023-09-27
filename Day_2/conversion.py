# Conversion from one data type to another data type 

# a = 123 
# print(type(a))

# print(70 + float("100.4")) #70 + 100.4 = 170.4
# print(str(40) + str(50)) # concatation of string takes place 




# Programe : WAP to that add the digit in a 2 digit number 
# Example : 35 => 3+5 = 8 

two_digit_number = input("Enter the number ")

# check the type of the 2-digit number 
type(two_digit_number)  #here type is string 

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

print(int(first_digit) + int(second_digit))  


