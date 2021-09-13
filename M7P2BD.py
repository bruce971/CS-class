#bruce diaz
#program will ask user for two inputs and then see if it is less than or greater than 10.

def evaluateInput1():
    input1 = input("Enter your first value")
    input2 = input("Enter your second value")

    if input1 + input2 > 10:
       print("your sum is greater than 10")
    if input1 + input2 < 10:
          print("your values are less than 10")
    if input1 + input2 == 10:
        print("your value is the same as 10")

        evaluateInput1()

    