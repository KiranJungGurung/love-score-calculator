# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


name = name1 + name2
name_lower_string = name.lower()

t = name_lower_string.count("t")
r = name_lower_string.count("r")
u = name_lower_string.count("u")
e = name_lower_string.count("e")

true = t + r + u + e

l = name_lower_string.count("l")
o = name_lower_string.count("o")
v = name_lower_string.count("v")
e = name_lower_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))
if (love_score < 10) and (love_score > 90):
  print(f"Your score is {love_score},you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"You score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}")
