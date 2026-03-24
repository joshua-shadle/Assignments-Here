#Joshua Shadle
#GPA program that takes a students last name and GPA to tell the student if they've made the Deans List or Honor Roll up to 5 people
number = 0
while number < 5:
    last_name = input("What is your last name?")
    if last_name == "ZZZ":
        break
    GPA = input("What is your GPA?, Please enter as a decimal with a floating point.")
    if float(GPA) >= 3.5:
        print(f"Congratulations {last_name.title()}, you have made the Dean's List.")
    elif float(GPA) < 3.5 and float(GPA) >= 3.25:
        print(f"Congratulations {last_name.title()}, you have made the Honor Roll.")
    else:
        print(f"I'm sorry,{last_name.title()} but your GPA is less than 3.25.")
    number += 1
