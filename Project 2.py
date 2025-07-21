print("Welcome to the time based greeting program!")
print("This program will greet you according to the time of the day")
print()
a = float(input("Enter the time in hours right now\nFor example: 13.20 {where 13 and 20 represent hour and minute respectively\nTime = "))

hours = int(a)
minutes = (a - hours) * 100

if 0 <= hours <= 23 and 0 <= minutes < 60:
    if 6.00 <= a < 12.00:
        print("Good Morning")
    elif 12.00 <= a <= 17.00:
        print("Good Afternoon")
    elif 17.01 <= a <= 19.59:
        print("Good Evening")
    elif 19.00 <= a <= 23.59 or 0.00 <= a <= 5.59:
        print("Good Night")
    else:
        print("Invalid time")
else:
    print("Invalid time")