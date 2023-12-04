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

# <-- main -->

if __name__ == '__main__':
  with open(dataSource, 'r') as file:
    for line in file.read().split('\n')[:-1]:
      print(line, end=" | ")
      print(extractNumerics(line))
      final += int(extractNumerics(line))

print("Sum:", final)
