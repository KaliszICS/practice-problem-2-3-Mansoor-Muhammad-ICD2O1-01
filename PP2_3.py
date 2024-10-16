

def q1(): 
  word = input("In: ")
  if word[-1:] == "y": 
    print("-ies")
  elif word[-2:] == "ey": 
    print("-eys")
  elif word[-3:] == "ife":
    print("-ives")
  else: 
    print("-s")


def q2(): 
  num = int(input("In: "))
  if num % 2 == 0:
    print(f"{num} is positive")
  elif num % 2 != 0:
    print(f"{num} is negative")
  else: 
    print("")

def q3():
  sidewon = input("Input a number: : ") 
  sidetwo = input("Input a number: ")
  sidethree = input("Input a number: ")
  if sidewon == sidetwo == sidethree:
    print("Equilateral")
  elif sidewon == sidetwo and sidewon != sidethree and sidewon == sidethree and sidewon != sidetwo:
    print("Isosceles")
  elif sidewon != sidetwo != sidethree:
    print("Scalene")
  else:
    print("No Triangle")
#Do not alter the following code
#Comment out the following code when running your tests
''' 
q1()
q2()
'''