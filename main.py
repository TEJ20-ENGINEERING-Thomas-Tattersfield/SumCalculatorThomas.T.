# asks user for input
User_number = int(input("Please input a positive interger: "))
# initializes I to 0 and shows how the new number is calculated
i = 0
New_number = i + 1 
# shows the formula and Calculations
while i < User_number:
  print ("{} + {} = {}". format (i, New_number, i + New_number))
  i += 1 