print ("This program is to determine whether someone is a minor, youth or elder!")

current_year = 2019
birth_year = input("Enter your birth year: ")
age = current_year - birth_year

if age < 18:
    print("You're minor!")
elif age >= 18 and age <= 36:
    print("You're a youth!")
else:
    print("You're an elder!")