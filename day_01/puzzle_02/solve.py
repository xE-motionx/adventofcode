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
# <-- vars -->
final = 0
dataSource = "./example"  # "./input" # "./example"
replace = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# <-- main -->

if __name__ == '__main__':
  with open(dataSource, 'r') as file:
    for line in file.read().split('\n')[:-1]:
      print(line + " > ", end="")
      for index, entry in enumerate(replace):
        line = line.replace(entry,str(index))
      print(line + " > ", end="")
      numericList = list(filter(str.isdigit, line))
      print(str(numericList[0]) + str(numericList[-1]))
      final += int((str(numericList[0]) + str(numericList[-1])))
  print("_____")
  print(final)
