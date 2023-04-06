# Functions - make sure to define a function before calling it

def print_name():
    text = "Bob loves cooking burgers."
    print(text)
    print(text)
    print(text)

print_name()

def print_slogan(text):
    print(text)

print_slogan("French fries are amazing!")

def school_age_calculator(age,name):
    if age < 5:
        print("Enjoy the time!", name, "is only" , age);
    elif age == 5:
        print("Enjoy kindergarten,", name);
    else: 
        print("They grow up so fast!");

school_age_calculator(5, "Ann")

def add_ten_to_age(age):
    new_age = age + 10
    return new_age

How_Old_Will_I_Be = add_ten_to_age(5);
print(How_Old_Will_I_Be);