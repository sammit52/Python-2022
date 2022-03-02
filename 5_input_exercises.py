#1
input("Press any key\n")
#2
input("Type out your name\n")
#3
input("Type out your age\n")
#4
user_name = input("What is your name?\n")
#5
user_age = int(input("What is your age?\n"))
#6
user_fav_movie = input("What is your favourite movie?\n")
#7
book = input("Name a book?\n")
#8
adjective = input("Name an adjective\n")
#9
noun = input("Name a noun\n")
#10
verb = input("Name a verb\n")
#11
book = input("Name a book?\n")
print(f"{book} is a decent book. I like the {noun} in it.")

noun = input("Name a noun\n")
print(f"{noun} is not a very descriptive word maybe put {adjective} infront of it.")

adjective = input("Name an adjective\n")
print(f"A {adjective} {noun}.")

user_age = int(input("What is your age?\n"))
print(f"{user_age} is pretty young, you have to be {user_age+7} to be here.")

user_name = input("What is your name?\n")
print(f"{user_name} is a {adjective} name. Is it scottish?")

input("Name a verb\n")
print(f"{verb} is a doing word. I like the way {user_fav_movie} symbolizes it.")

user_fav_movie = input("What is your favourite movie?\n")
print(f"{user_fav_movie} is a {adjective} movie that won 7 oscars.")

money = input("How much money do you have?\n")
print(f"{money}??!?!? You are very poor compared to the main character in {user_fav_movie}.")
#12
user_age = input("How old are you?\n")
#13
print(f"You will be {user_age+10} in ten years!")
#14
print(f"You were born in {2022-user_age}.")
#15
user_apples = int(input("How many apples do you have?\n"))
#16
user_friends = int(input("How many friends do you have?\n"))
#17
if int(user_apples/user_friends) > 1:
	apple_grammatical_number = "apples"
elif int(user_apples/user_friends) == 0:
	apple_grammatical_number = "apples"
else:
	apple_grammatical_number = "apple"

print(f"If you shared your apples with your friends they would have {int(user_apples/user_friends)} {apple_grammatical_number}! And you would have {user_apples%user_friends} apples left over")
#18
user_pizza = int(input("How many pizzas do you want?\n"))
#19
people_feeding = int(input("How many people are you feeding?\n"))
#20
print(f"Each person will get {int((user_pizza*8)/people_feeding)} slices. You will then have {(user_pizza*8)%people_feeding} slices left over.")
#21
user_money = int(input("How much money do you have?\n"))
#22
tv_cost = int(input("How much does a TV cost?\n"))
#23
print(f"You will have {user_money-tv_cost} dollars leftover.")
#24
print(f"You will save {tv_cost-(tv_cost*0.8)} dollars if you wait for a 20% off sale!")
#25
user_bitcoin = int(input("How much bitcoin do you have?\n"))
#26
bitcoin_value = 65136.75
#27
print(f"Your bitcoin portfolio is worth {user_bitcoin*bitcoin_value} dollars!")
#28
user_weekly_money = int(input("How much money do you make a week?\n"))
#29
tax_rate = int(input("What is your tax rate?\n"))
#30
print(f"You will have {user_weekly_money*((int(100-tax_rate))/100)} dollars after tax")
#31
user_book = input("Name a book\n").lower()
#32

print(f"{user_book}")

user_book = user_book.upper()

print(f"{user_book}")

user_book = user_book.title()

print(f"{user_book}")
#33
user_number = int(input("Name a number\n"))
#34
print(f"{user_book*user_number}")