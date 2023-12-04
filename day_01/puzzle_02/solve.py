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
# <-- main -->

if __name__ == '__main__':
  with open(dataSource, 'r') as file:
    for line in file.read().split('\n')[:-1]:
      extractNumericValues(line)
