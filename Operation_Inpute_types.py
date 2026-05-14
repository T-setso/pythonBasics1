#Capture information of 2 users. This information includes their name, age and height (in cm).
user1 = input("Please enter your name: ")
age_user1 = input("Please enter your age: ")
height_user1 = input("Please enter your height in cm: ")
print()

#print(user1)
user2 = input("Please enter your name: ")
age_user2 = input("Please enter your age: ")
height_user2 = input("Please enter your height in cm: ")

#Display each user&#039;s information in a sentence format.
print(f"My name is {user1} I'm {age_user1} years old, and my height is {height_user1}cm.")
print(f"My name is {user2} I'm {age_user2} years old, and my height is {height_user2}cm.")
print()

#Then calculate and display the total combined height of both users.
sum_height = int(height_user1) + int(height_user2)
print(f"The total combined height is {sum_height} ")