# Program is made to encode or decode secret messages.

# Making a list of the alphabets.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

""" Defining a function with 3 arguments. One for the text we are receiving, one is the amount of shifts we are going and direction is for whether we are encoding
or decoding. 
"""
def caesar(new_text, num_shifts, main_direction):
  # Made a blank list for the output message once it's ready to receive the encoded or decoded message.
  main_cipher_text = ""
  decodenew_position = 0
  # Made a for loop so that every letter (char) that is received from the input message is being checked.
  for char in new_text:
    # If the letter is in the alphabet it will start in the position of the alphabets
    if char in alphabet:
      position = alphabet.index(char)
      # If the user chooses 'decode' it will subtract (go backwards) from the position to give a new letter in that position.
      if main_direction == "decode":
      # The position is given a new position by subtracting the amount of shifts according to what the user input. Uses a modulus to never pass 26 to avoid index error.
        new_position = (position - num_shifts) % 26
      # otherwise user chooses 'encode' which adds the amount of shifts with the modulus of 26 so we avoid index errors.
      elif main_direction == "encode":
        new_position = (position + num_shifts) % 26
      # the empty list is now given the new letters based on message, the encode/decode user input, and amount of shifts into the message thats been encoded or decoded.
      main_cipher_text += alphabet[new_position]
    else:
      # this part allows us to give spaces into our messages. So instead it going through the decoding or encoding process it will just see it as a space.
      main_cipher_text += char
  print(f"the {main_direction} text is {main_cipher_text} ")
        
code_is_looping = True

"""
The while loop is what makes the program run until the user decides not to use it again after encoding or decoding.
"""

# Coding_is_Looping is True right now.
while code_is_looping:
  
  # User chooses whether to encode or decode, the message they want to decrypt/encrypt, as well as the amount of shifts forward or backwards. 
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  # Running the function with the arguments mentioned above.
  caesar(new_text=text,num_shifts=shift,main_direction=direction)
  
  # If user chooses to continue after the function is done, the While loop remains True and the program keeps going.
  yes_no = input("Would you like to continue?[y,n]").lower()
  if yes_no == 'y':
    code_is_looping = True
  # If the user chooses to stop it after by pressing 'n' after the function is ran. The Whole loop will be False ending the program. 
  elif yes_no == 'n':
    print("Thank you for using this program...\nGoodbye!")
    code_is_looping = False
  # If user presses anything that is not 'y' or 'n' we let the user know they typed an invalid entry which loops the while loop over again.
  else:
    print("You entered invalid entry")
    code_is_looping = True

