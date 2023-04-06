# While loop

x = 0
while (x<5):
    print(x)
    x = x + 1

# For loop 

for x in range(5,10):
    print(x)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for d in days: 
    if(d=="Thu"):break
    print(d)

for d in days: 
    if(d=="Thu"):continue
    print(d)
