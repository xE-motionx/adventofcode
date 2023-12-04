#!/usr/bin/python3
############## ## # # # #  #  #        #
# Author: Frederik Brönner
# Date: 2023.12.01
# AOC:  01
# Problem description:
#   Rows of input. First and last diget meant to form a two-digit number
#   Identify and combine digits to new value.
#   However, written digits now count, too. :|
###### ##  ## # # # # # #     ##   #

# <-- imports -->
<<<<<<< HEAD
import re

# <-- functions -->

def extractNumericValues(string_in):
  numerics = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  resolvedNumerics = ""
  for index, character in enumerate(string_in):
    if character.isnumeric():
      resolvedNumerics += character
    else:
      print(string_in[index:])

  print("X:" + resolvedNumerics)

# <-- vars -->
final = 0
dataSource = "./example"  # "./input" # "./example"
=======

# <-- functions -->

def extractNumerics(string):
  numericValues = ""
  values = ['zero', 'one', 'two', 'three', 
             'four', 'five', 'six', 'seven', 
             'eight', 'nine', 'ten', 'eleven', 
             'twelfe','thirteen']
  for index_s,char in enumerate(string):
    numeric = ""
    if char.isnumeric():
      numericValues += char
    else:
      for index_v,value in enumerate(values):
        if string[index_s:].startswith(value):
          numeric = str(index_v)
          numericValues += str(index_v)
      if string[index_s:].startswith("teen"):
        numericValues = numericValues[:-1] + "1" + numericValues[-1:]
  return numericValues[0] + numericValues[-1:]  

# <-- vars -->
final = 0
dataSource = "./input"  # "./input" # "./example"

>>>>>>> 2315c37126dbc3708f290a69adbdf5037398694c
# <-- main -->

if __name__ == '__main__':
  with open(dataSource, 'r') as file:
    for line in file.read().split('\n')[:-1]:
<<<<<<< HEAD
      extractNumericValues(line)
=======
      print(line, end=" | ")
      print(extractNumerics(line))
      final += int(extractNumerics(line))

print("Sum:", final)
>>>>>>> 2315c37126dbc3708f290a69adbdf5037398694c
