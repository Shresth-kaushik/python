# Caesar cipher text challange  ::

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# Step 1 + 2 : 

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#e.g. 
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.  


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text , shift_amount):
    cipher = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher+= new_letter
    print(f"The encrypted text {cipher}")



# Decryption of the txt  : -> same steps as encrytion 
def decrypt(plain_text , shift_amount):
    text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        text+= new_letter
    print(f"The decrypted text {text}")


if direction == "encode":
    encrypt(plain_text = text , shift_amount = shift)
elif direction == "decode":
    decrypt(plain_text = text , shift_amount = shift)    


# Optimized code of the problem :

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#       shift_amount *= -1
#   for letter in start_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
#   print(f"Here's the {direction}d result: {end_text}")


# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)



# ----------------------------->>> <<<-------------------------------------------

# Optimization : 
# If the shift amount entered in greater than the 26 than what 
#  so , solution is shift = shift % 26 

# 