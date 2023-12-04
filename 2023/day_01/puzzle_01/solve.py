#!/usr/bin/python3
############## ## # # # #  #  #        #
# Author: Frederik Brönner
# Date: 2023.12.01
# AOC:  01
# Problem description:
#   Rows of input. First and last diget meant to form a two-digit number
#   Identify and combine digits to new value.
###### ##  ## # # # # # #     ##   #

# <-- imports -->

# <-- functions -->

def extractNumericValues(string_in):
  for character in string_in:
    print(character)


# <-- vars -->
final = 0
dataSource = "./input" # "./example"

# <-- main -->

if __name__ == '__main__':
  with open(dataSource, 'r') as file:
    for line in file.read().split('\n')[:-1]:
      numericList = list(filter(str.isdigit, line))
      print(str(numericList[0]) + str(numericList[-1]) + "   (" + line + ")")
      final += int((str(numericList[0]) + str(numericList[-1])))
  print("_____")
  print(final)
