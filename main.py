# asks user for input
User_number = int(input("Please input a positive interger: "))
# initializes I to 0
i = 0
# shows the formula and Calculations
while i <= User_number:
  print ("{} * {} = {}". format (i, User_number, i * User_number))
  i += 1 