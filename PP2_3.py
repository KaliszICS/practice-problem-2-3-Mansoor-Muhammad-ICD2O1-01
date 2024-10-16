

def q1(): 
  word = input("In: ")
  if word[-3:] == "ife":
    print("-ives")
  elif word[-2:] == "ey": 
    print("-eys")
  elif word[-1:] == "y": 
    print("-ies")
  else: 
    print("-s")


def q2(): 
  num = int(input("In: "))
  if num > 0:
    print(f"{num} is positive")
  elif num < 0:
    print(f"{num} is negative")
  

def q3():
  sidewon = float(input("Input a number: ")) 
  sidetwo = float(input("Input a number: "))
  sidethree = float(input("Input a number: "))
  if sidewon + sidetwo > sidethree and sidewon + sidethree > sidetwo and sidetwo + sidethree > sidewon:
    if sidewon == sidetwo == sidethree:
      print("Equilateral")
    elif sidewon == sidetwo or sidewon == sidethree or sidetwo == sidethree:
      print("Isosceles")
    else: 
      print("Scalene")
  else:
    print("No Triangle")
#Do not alter the following code
#Comment out the following code when running your tests
''' 
q1()
q2()
'''
