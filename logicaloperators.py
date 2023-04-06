print(1+1);
print(1-1);
print(1*1);
print(1/1);
print(1//1);
print(1%1);

# Logical Operators 

# == Equal to
# != Not Equal to 
# < Less than 
# > Greater than 
# >= Greater than or equal to 
# <= Less than or equal to 

Bob_Age = 13
Age_at_Kindergarten = 5
Age_at_elementary_school = 6
Age_at_high_school = 13

# if/elif/else statement 

if Bob_Age == Age_at_Kindergarten: 
    print("Bob is in kindergarten!");
elif Bob_Age >= Age_at_elementary_school and Bob_Age < Age_at_high_school:
    print("Bob is somewhere in elementary school!");
elif Bob_Age >= Age_at_high_school:
    print("Bob is in high school!");
else:
    print("Bob is not in school!");