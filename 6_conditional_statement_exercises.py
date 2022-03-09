"""
#1
icecream_order = int(input("How many icecreams do you need?\n"))

if icecream_order > 20:
	print("There is not enough icecream in stock.")
elif icecream_order == 1:
	print("Thankyou for ordering an icecream!")
else:
	print(f"Thankyou for ordering {icecream_order} icecreams!")

#2
travel_distance = int(input("How far are you intending to travel?\n"))

if travel_distance > 200:
	print(f"You do not have enough fuel to travel {travel_distance} kilometres")
else:
	print(f"You have enough fuel to travel {travel_distance} kilometres")

#3
user_age = int(input("How old are you?\n"))

if user_age >= 18:
	print("You are considered an adult")
else:
	print("You are a minor")

#4
user_fav_movie = input("What is your favourite movie").lower()

if user_fav_movie == "lord of the rings":
	print("You have an excellent taste in films")
else:
	print(f"I regret to inform you that the Lord of the Rings is clearly a superior film too {user_fav_movie}")


#5
darth_plaguesis_question = input("Have you heard of the tradegy Darth Plaguesis the Wise?").lower()

if darth_plaguesis_question == "no":
	print("t’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.")
else:
	print("You must be a fan!")

#6
passion_of_christ_question = input("Who directed Passion of the Christ?").lower()

if passion_of_christ_question == "mel gibson":
	print("Correct")
else:
	print("Mel Gibson did")
"""
#7
score = 0

question1 = input("What is 7x7?\n[A] 7^2, [B] 69, [C] 49, [D] 420\n").upper()

if question1 == "A" or "7^2" or "C" or "49":
	score = score + 1
	print("Correct!")
else:
	print("Wrong. The answer was A or C")

question2 = input("What is √9\n[A] 3^2, [B] 3, [C] 81, [D] 69").upper()

if question2 == "B" or "3":
	score = score + 1
	print("Correct!")
else:
	print("Wrong. The right answer was B")

question3 = input("What is x/x\n[A] x, [B] 1, [C] x^2, [D] 69").upper()

if question3 == "B" or "1":
	score = score + 1
	print("Correct!")
else:
	print("Wrong. The right answer was B")

question4 = input("What is log(100)\n[A] 2, [B] 1, [C] 10, [D] 69").upper()

if question4 == "A" or "2":
	score = score + 1
	print("Correct!")
else:
	print("Wrong. The right answer was A")

question5 = input("What is ((((6^2 * 10) + sqrt((5000*3) - 600)) / 4! ) * 4 ) - log(1 * 10^11)\n[A] 10236.2391, [B] 0, [C] 2log(e), [D] 69").upper()

if question5 == "D" or "69":
	score = score + 1
	print("Correct!")
else:
	print("Wrong. The right answer was D")

print(f"You scored {score} out of 5!")