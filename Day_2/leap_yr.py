# divisible by 4 , 100 , 400 => leap yr hai
# if not by 4 -> not a leap yr 
# if divisble by 4 and not divisible by 100 =>  leap yr 
# if by 4 , if by 100 then must be divisible by 400 => for a leap yr.


year = int(input("Enter the year "))

if year%4 ==0:
    if year%100==0:
        if year%400==0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")        
else:
    print("Not a leap year")