# Dictionaries : key -> value pairs are present 

programming_dictinory = {
    "bug" : "The error in the programme that prevent the prg from running as expected" , 
    "function" :"which we can call again and again " 
}

# Excessing the data/value  from the
print(programming_dictinory["bug"]) 

# how to add the new entry in the dictinory ? 
programming_dictinory["loop"] = "The action of doing something again and again "

# creating the empty dict. 
empty_dict = { }

# wipe an existing dict. 
# programming_dictinory ={ }
# print(programming_dictinory)


# Edit an item in the dictinory 
programming_dictinory["bug"] = "this is a bug value "
print(programming_dictinory["bug"])
print("\n")

# loop through dictinory  -> Just give the key as output
for i in programming_dictinory:
    print(i)