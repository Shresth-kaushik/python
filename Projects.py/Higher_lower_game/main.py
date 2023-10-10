import art_h_l
from game_data import data
import random
import os
# from replit import clear

# We have to create a function to access the data varibles from the dictinary ,
def format_data(account):
    '''Takes the account data and return it into printable format '''
    account_name = account["name"]
    account_desc = account["description"] 
    account_country = account["country"]
    return (f"{account_name} , a {account_desc} form  {account_country} ")


def check_guess(guess , account_a_followers  , account_b_followers):
    '''Check whether the guess by the user is correct or not '''
    if account_a_followers > account_b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


# print the logo 
print(art_h_l.logo)
score = 0
game_continue = True

# For the looping of the account i.e =  
account_b = random.choice(data)

while game_continue:
    # Generate the random data from the game data for the 2 account , 
    # we have to compare the 2 account .  
    account_a = account_b
    account_b = random.choice(data)
    # if both account choosen is same then ?
    if(account_a == account_b):
        account_b = random.choice(data)


    # printing the comparasion of the 2 accout data
    print(f"Compare A: {format_data(account_a)} ")

    # print the vs logo 
    print(art_h_l.vs)

    print(f"Against B: {format_data(account_b)} ") 

    # User guess from either of the account => which has more followers .
    guess = input("Who has more followers ? Type A or B : ").lower()

    # Check the guess =>
    # Get the followers of the both account 
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = check_guess(guess , account_a_followers=a_followers ,account_b_followers=b_followers)

    os.system('clear')

    # Score track and the feedback to the user :
    if is_correct:
        score+=1
        print(f"You're right ! current score is {score} ")
    else:
        game_continue = False
        print(f"Sorry , you're wrong ! Final score is {score} ")

        
            









