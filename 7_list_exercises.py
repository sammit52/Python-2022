
#1
fibonacci_sequence = [0,1,1,2,3,5,8,13,21,34]
print(fibonacci_sequence)
#2
fav_fruits = ["apple","plums","peach","green apple","strawberries"]
print(fav_fruits)
#3
youtubers = ["Mark Rober","Kurgesagt In A Nutshell", "Sciencephile The AI", "Infinityplusone"]
print(youtubers)
#4
songs = []
songs.insert(0,"Runaway")
print(songs)
songs.insert(0,"No Role Modelz")
print(songs)
songs.insert(0,"Good Morning")
print(songs)
songs.insert(0,"Middle Child")
print(songs)
songs.insert(0,"Its You")
print(songs)

#5
books = []
books.append(input("What is your favourite book?\n"))
print(books)
books.append(input("What is your second favourite book?\n"))
print(books)
books.append(input("What is your third favourite book?\n"))
print(books)
books.append(input("What is your fourth favourite book?\n"))
print(books)
books.append(input("What is your fifth favourite book?\n"))
print(books)

#6
pizza_toppings = []
toppings = 0

topping = input("Add a topping to the pizza\n")
if topping != "":
	pizza_toppings.append(topping)
topping = input("Add a topping to the pizza\n")
if topping != "":
	pizza_toppings.append(topping)
topping = input("Add a topping to the pizza\n")
if topping != "":
	pizza_toppings.append(topping)
topping = input("Add a topping to the pizza\n")
if topping != "":
	pizza_toppings.append(topping)
topping = input("Add a topping to the pizza\n")
if topping != "":
	pizza_toppings.append(topping)
topping = input("Add a topping to the pizza\n")
if topping != "":
	pizza_toppings.append(topping)
print(f"So the toppings for your pizza are: {pizza_toppings}")

#7
fruits = ["apple","banana","tomatoe","pear","plum"]
user_fruit = input("Name a fruit to add to the list\n").lower()

if user_fruit not in fruits:
	fruits.append(user_fruit)
	print(fruits)
else:
	print("That fruit is already on the list!")

#8
names = ["Maximus Holgatus","Deez","Mike Ockslong"]
print(f"{names}")
names.reverse()
print(f"{names}")

#9
prime_numbers = [ "2", "3", "7", "5", "11", "13", "17", "23", "19", "29", "31", "37", "41", "43", "47", "53", "59", "61", "67", "71" ]
prime_numbers.sort()
prime_numbers.reverse()
print("The length of list is: ", len(prime_numbers))

#10

verbs = ["Running","Doing","Walking","Eating","Looking"]
verbs.sort()
print(verbs)





