#Import the necessary libraries
import re
from simpleai.search import CspProblem, backtrack

#Print some text to indicate when and what to insert
print("Enter your puzzle here... (like this: TO + GO = OUT)")

#Put the input in a variable 'puzzle', change all letters to uppercase and remove the spaces using the re library
puzzle = input().upper()
puzzle_no_spaces = re.sub(" ", "", puzzle)

#Search the kind of method used
for letter in puzzle_no_spaces:
  if letter in ["+", "-", "*", "/"]:
    method = letter

#Identify the different parts of the puzzle
#First part until the method
part1 = tuple(puzzle_no_spaces[:puzzle_no_spaces.index(method)])
#Second part between the method and the equal sign
part2 = tuple(puzzle_no_spaces[puzzle_no_spaces.index(method)+1:puzzle_no_spaces.index("=")])
#Third part after the equal sign
part3 = tuple(puzzle_no_spaces[puzzle_no_spaces.index("=")+1:])

#Remove the signs from the puzzle with the re library
clean_puzzle = re.sub("[-+*/=]", "", puzzle_no_spaces)

#Create a domain variable, where we will add the values later on
domains = {}

#Empty list, where we will add all letters to later on
chars=[]

#Loop over the first part of the puzzle
#If we come across the first letter ->
#a list from 1 to 10 (10 excluded) will be added to the domains variable
#If it is not the first letter ->
#a list from 0 to 10 (10 excluded) will be added to the domains variable
for letter in part1:
  if letter == part1[0]:
    domains[letter] = list(range(1,10))
    chars.append(letter) #Letter will be added to the chars variable
  else:
    domains[letter] = list(range(0,10))
    chars.append(letter) #Letter will be added to the chars variable

#Loop over the second part of the puzzle
#If we come across the first letter ->
#a list from 1 to 10 (10 excluded) will be added to the domains variable
#If it is not the first letter ->
#a list from 0 to 10 (10 excluded) will be added to the domains variable
for letter in part2:
  if letter == part2[0]:
    domains[letter] = list(range(1,10))
    chars.append(letter) #Letter will be added to the chars variable
  else:
    domains[letter] = list(range(0,10))
    chars.append(letter) #Letter will be added to the chars variable

#Loop over the third part of the puzzle
#If we come across the first letter ->
#a list from 1 to 10 (10 excluded) will be added to the domains variable
#If it is not the first letter ->
#a list from 0 to 10 (10 excluded) will be added to the domains variable
for letter in part3:
  if letter == part3[0]:
    domains[letter] = list(range(1,10))
    chars.append(letter) #Letter will be added to the chars variable
  else:
    domains[letter] = list(range(0,10))
    chars.append(letter) #Letter will be added to the chars variable

#Remove all duplicates from the chars variable
chars = list(set(chars))

#Create the constraints

#Create a constraint to verify if all characters are unique
#by comparing the length of the filtered list with the normal list
def constraint_unique(chars, values):
  return len(values) == len(set(values))

#Create a constraint to ensure that factor1 + factor2 = result
def constraint_add(chars, values): #Kan geen 3 lijsten aanpakken, dus chars ipv characters1,2,3. En al helemaal niet de variables die der eerst stond, want die hebben geen waarde (niet aangeroepen in domains)
  #We create 3 variables which we will later on use in our for loops
  factor1 = ""
  factor2 = ""
  result = ""

  #Loop over the first part of the puzzle and add each letter to the factor1 variable
  for letter in part1:
    index = chars.index(letter)
    factor1 += str(values[index])
  
  #Loop over the second part of the puzzle and add each letter to the factor2 variable
  for letter in part2:
    index = chars.index(letter)
    factor2 += str(values[index])

  #Loop over the third part of the puzzle and add each letter to the result variable
  for letter in part3:
    index = chars.index(letter)
    result += str(values[index])

  #Convert these factors to integer, so we can calculate with them
  factor1 = int(factor1)
  factor2 = int(factor2)
  result = int(result)

  #We add the 2 factors together which must equal the result
  return (factor1 + factor2) == result

#Create a constraint to ensure that factor1 - factor2 = result
def constraint_substract(chars, values):
  #We create 3 variables which we will later on use in our for loops
  factor1 = ""
  factor2 = ""
  result = ""

  #Loop over the first part of the puzzle and add each letter to the factor1 variable
  for letter in part1:
    index = chars.index(letter)
    factor1 += str(values[index])
  
  #Loop over the second part of the puzzle and add each letter to the factor2 variable
  for letter in part2:
    index = chars.index(letter)
    factor2 += str(values[index])

  #Loop over the third part of the puzzle and add each letter to the result variable
  for letter in part3:
    index = chars.index(letter)
    result += str(values[index])

  #Convert these factors to integer, so we can calculate with them
  factor1 = int(factor1)
  factor2 = int(factor2)
  result = int(result)

  #We substract factor 2 from factor 1 which must equal the result
  return (factor1 - factor2) == result

#Create a constraint to ensure that factor1 * factor2 = result
def constraint_multiply(chars, values):
  #We create 3 variables which we will later on use in our for loops
  factor1 = ""
  factor2 = ""
  result = ""

  #Loop over the first part of the puzzle and add each letter to the factor1 variable
  for letter in part1:
    index = chars.index(letter)
    factor1 += str(values[index])
  
  #Loop over the second part of the puzzle and add each letter to the factor2 variable
  for letter in part2:
    index = chars.index(letter)
    factor2 += str(values[index])

  #Loop over the third part of the puzzle and add each letter to the result variable
  for letter in part3:
    index = chars.index(letter)
    result += str(values[index])

  #Convert these factors to integer, so we can calculate with them
  factor1 = int(factor1)
  factor2 = int(factor2)
  result = int(result)

  #We multiply factor 1 with factor 2 which must equal the result
  return (factor1 * factor2) == result

#Create a constraint to ensure that factor1 / factor2 = result
def constraint_divide(chars, values):
  #We create 3 variables which we will later on use in our for loops
  factor1 = ""
  factor2 = ""
  result = ""

  #Loop over the first part of the puzzle and add each letter to the factor1 variable
  for letter in part1:
    index = chars.index(letter)
    factor1 += str(values[index])
  
  #Loop over the second part of the puzzle and add each letter to the factor2 variable
  for letter in part2:
    index = chars.index(letter)
    factor2 += str(values[index])

  #Loop over the third part of the puzzle and add each letter to the result variable
  for letter in part3:
    index = chars.index(letter)
    result += str(values[index])

  #Convert these factors to integer, so we can calculate with them
  factor1 = int(factor1)
  factor2 = int(factor2)
  result = int(result)

  #We substract factor 2 from factor 1 which must equal the result
  return (factor1 / factor2) == result

#If the + was used, we use the constraint_add
if method == "+":
  constraints = [
    #Use all characters in the puzzle together with the constraint_unique to ensure they are unique
    (chars, constraint_unique),
    #Use all characters in the puzzle together with the constraint_add to ensure factor1 + factor2 equals result
    (chars, constraint_add), 
  ]

#If the - was used, we use the constraint_substract
elif method == "-":
  constraints = [
    #Use all characters in the puzzle together with the constraint_unique to ensure they are unique
    (chars, constraint_unique),
    #Use all characters in the puzzle together with the constraint_substract to ensure factor1 - factor2 equals result
    (chars, constraint_substract),
  ]

#If the * was used, we use the constraint_multiply
elif method == "*":
  constraints = [
    #Use all characters in the puzzle together with the constraint_unique to ensure they are unique
    (chars, constraint_unique),
    #Use all characters in the puzzle together with the constraint_multiply to ensure factor1 * factor2 equals result
    (chars, constraint_multiply),
  ]

#If the / was used, we use the constraint_divide
elif method == "/":
  constraints = [
    #Use all characters in the puzzle together with the constraint_unique to ensure they are unique
    (chars, constraint_unique),
    #Use all characters in the puzzle together with the constraint_divide to ensure factor1 / factor2 equals result
    (chars, constraint_divide),
  ]

#If no valid method was used we return "No valid method"
else:
  print("No valid method")


#Use the CspProblem library and the backtrack library to solve the problem
problem = CspProblem(chars, domains, constraints)
output = backtrack(problem)

#Check if there is a solution
#When a solution is found, print it in the right format
if output:
  #Create an empty solved_puzzle variable, where we will later on add letters to
  solved_puzzle = ""
  #Loop over all the letters in the puzzle and add the corresponding value from the solution to the solved_puzzle variable
  for letter in puzzle:
    if letter in output:
      solved_puzzle += str(output[letter])
      #If we come across a space, +, -, *, /, =, we just add them as they are
    elif letter in ["+", "-", "*", "/", "=", " "]:
      solved_puzzle += letter
  #Print out the original and the converted one
  print(puzzle, "->", solved_puzzle)
  #Loop over all the keys in the solution and print their corresponding values
  for key in output:
    print(key, "=", output[key])
#When no solution is found, print "No solution found"
else:
  print("No solution found")
