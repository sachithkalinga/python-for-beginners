
def students(subject, marks, friends):
    print("Subject: ", subject)
    print("Marks: ", marks)
    print("Friends: ", friends)

students("Maths", 68, "Kevin")
# Subject:  Maths
# Marks:  68
# Friends:  Kevin

#Default arguments...............................................................
print("\n")

def students(subject = "Physics", marks = 30, friends = "Ann"):
    print("Subject: ", subject)
    print("Marks: ", marks)
    print("Friends: ", friends)

students("Maths")
# Subject:  Maths
# Marks:  30
# Friends:  Ann
print("\n")

def students(subject, marks, *friends):
    print("Subject: ", subject)
    print("Marks: ", marks)
    print("Friends: ", friends)

students("Maths", 68, "Kevin", "Snoop", "Dre")
# Subject:  Maths
# Marks:  68
# Friends:  ('Kevin', 'Snoop', 'Dre')
print("\n")

def students(subject, marks, **friends):
    print("Subject: ", subject)
    print("Marks: ", marks)
    print("Friends: ", friends)

students("Maths", 68, Kevin = 45, Snoop = 65, Dre = 80)
# Subject:  Maths
# Marks:  68
# Friends:  {'Kevin': 45, 'Snoop': 65, 'Dre': 80}
print("\n")

def students(subject, marks, **friends):
    print("Subject =", subject)
    print("Marks =", marks)
    for key, value in friends.items():
        print(key, "=", value)

students("Maths", 68, Kevin = 45, Snoop = 65, Dre = 80)
# Subject = Maths
# Marks = 68
# Kevin = 45
# Snoop = 65
# Dre = 80