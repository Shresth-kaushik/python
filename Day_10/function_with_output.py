# Function with output 

def function_(f_name  , l_name):
    first_name = f_name.title()
    last_name = l_name.title()

    return f"The first name is {first_name} and last name {last_name}"

output = function_("AnKit" , "KausHIK")  
print(output) 


# # Docstring : 
#  Declared just after the function => indentend code .
# """"  """" -> syntax 

# Python documentation strings (or docstrings) provide a convenient way of 
# associating documentation with Python modules, functions, classes, and methods. 
# It’s specified in source code that is used, like a comment, to document a
#  specific segment of code. Unlike conventional source code comments, the
#  docstring should describe what the function does, not how.

# Declaring Docstrings: The docstrings are declared using ”’triple single quotes”’ or 
# “”” triple double quotes “”” just below the class, method, or function
#  declaration. All functions should have a docstring.
# Accessing Docstrings: The docstrings can be accessed using the __doc__ 
# method of the object or using the help function. The below examples 
# demonstrate how to declare and access a docstring.