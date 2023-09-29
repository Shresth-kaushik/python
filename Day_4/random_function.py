# random module is used to generate the random value in between certain range 
import random
import my_module # to use the function present in the my_module file in this file /

random_int = random.randint(1,20)
print(random_int)

print(my_module.pi)

random_float = random.random()
print(random_float)