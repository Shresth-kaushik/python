# If statement do not have their particular block 
game_level = 3
enemies = ["amit" , "aksh" , "Alice "]

if game_level < 5:
    new_enemies = 4
    print(enemies[1])

# here we can access the new_enemies outside of the scope .
print(new_enemies) # ouput as 4