

def get_message(message):
    if message > 1000:
        print("Your message box is full...")
    print("You have new message!")

all = 900
get_message(all)



def user_state(state):
    print(f"Bob: {state}")

user_state("Active")

#Returning Value............................................

def half_twice(number):
    half = number/2
    half_again = half/2
    return half_again

result = half_twice(10)
print(result)

#Multiple parameters.........................................

def mix(first, second, third):
    print(f"{first} {second} {third}")

ans = mix("Happy", "Birthday", "!!!")


def students(subject, marks, *friends):                
    print("Subject: ", subject)
    print("Marks: ", marks)
    print("Friends: ", friends)
    
students("Math", 80, "Ann", "John")

""" Subject:  Math
        Marks:  80
        Friends:  ('Ann', 'John')  
"""

def students(subject, marks, **friends):                
    print("Subject: ", subject)
    print("Marks: ", marks)
    print("Friends: ", friends)
    
students("Math", 80, Ann = 50, John = 75)

""" Subject:  Math
    Marks:  80
    Friends:  {'Ann': 50, 'John': 75}
"""