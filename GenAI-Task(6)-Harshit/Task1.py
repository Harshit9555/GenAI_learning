#Safe Division Utility
numerator  = int(input("Enter Numerator"))
denominator  = int(input("Enter Denominator"))
try:
    result = numerator/denominator
except ValueError as ex1:
    print("Input is not number:",ex1)
except ZeroDivisionError as ex2:
    print("Denominator is 0:",ex2)
else:
    print("The result is: ",result)
finally:
    print("Operation Completed")
    
    