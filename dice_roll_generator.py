# This is a dice roll generator python program.

# importing random module which is used to generate random numbers
import random
# importing os module which provides functionality (such as input/output, 
# creating files) to interact with the
# operating system
import os

# Declaring a function names num_die with no arguments
def num_die():
# Creating a while loop to indefinitely repeat the below block of code.
  while True:
# We are putting try and except statement that if try fails, then except
# will execute the function.
      try:
          num_dice = input(' Write number of dice: ')
          valid_responses = ['1', 'one', 'two', '2']
          if num_dice not in valid_responses:
              raise ValueError('1 or 2 only')
          else:
              return num_dice
      except ValueError as err:
          print(err)