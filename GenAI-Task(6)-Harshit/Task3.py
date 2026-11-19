#Custom Exception: Age Validator
def check_age(age):
    try:
        if age <1 or age >120:
            raise ValueError("Age must be between 1 and 120")
    except Exception as ex:
        print("Invalid  age")
    else:
        print(f"Age is {age}")

age = int(input("Enter the Age:"))
check_age(age)
