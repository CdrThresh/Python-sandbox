# Practice of printing text

print("hello world");
print( "you there" )

#Strings/Variable assignment

rock = "Malphite";
print(rock);
water = "aqua";
print(water);
paper = "Cardboard";
del paper;
paper = 6;
print(type(paper));

#Input 

# cup = input("What do you want to put in the cup? ");
# print(cup);

# Converting variable types 

# birth_year = input("Enter the year you were born: ");
# age = 2023 - int(birth_year);
# print(age)

# Adding two numbers based on user input 

# First_number = input("What is your first number?");
# Second_number = input("What is your second number?");
# New_number = int(First_number) + int(Second_number);
# print(New_number);

# First_number = float(input("What is your first number?"));
# Second_number = float(input("What is your second number?"));
# New_number = First_number + Second_number
# print("Sum: " + str(New_number));

# Methods

course = "Python for Beginners";
print(course.upper())
print(course.find('y'))
print(course.replace('for', '4'));
print('Python' in course)

# Weight Conversion program 

User_weight = int(input("Weight: "));
Poundage = input("Kg or Lbs: ");

if Poundage.upper() == "Kg" or Poundage.upper() == "K":
    converted = User_weight / 0.45;
    print("Weight in Lbs: " + str(converted));
else: 
    converted = User_weight * 0.45
    print("Weight in Kgs: " + str(converted));
    
