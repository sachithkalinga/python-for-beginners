if True:
    print("Hello world")

if False:
    print("Hello world")

if 5>2:
    print("Yes")

if 5 > 50:
    print("No")

# .....................................................

greet = True
if greet:
    print("Greetings...!")

is_charge = False
if is_charge:
    print("Battery Full")
else:
    print("Battery law")

# .......................................................

answer1 = "January"
if answer1 != "January":
    print(f"This month is {answer1}.")
print(f"This month is not {answer1}.")

answer2 = "January"
if not answer2:
    print(f"This month is {answer2}.")
print(f"This month is not {answer2}.")

# ........................................................
points = 50
points_need = 100

if points == points_need:
    print("You qualified to next level.")
elif points > points_need:
    print("You're over qualified to next level.")
else:
    print(f"You need {points_need - points} more points to next level")

points = 50
points_need = 100

print("You qualified to next level.") if points == points_need else print(f"You need {points_need - points} more points to next level")
