###################################
#IMPORTS
###################################
from adventurelib import *
import time
###################################
#DEFINE ROOMS
###################################
Bedroom1 = Room("You are in dull lit room. There is a bed, draws with a broken handle and a cupboard in the back corner. The only exit appears to be a big metal door.")
Lounge = Room("You are in the living area. It has 2 barred windows. There is a big battered couch, tv and shelf.")
Dining_Room = Room("There is a table in the center of the room with no windows. Around lay scattered chairs and on it are some papers.")
Kitchen = Room("You are in a kitchen. There is a fridge and some cabinents. The fridge is decorated with magnets.")
Hallway = Room("You are in dull lit hallway. There is nothing but a depressing painting hanging on the wall.")
Bedroom2 = Room("You are in a room. There is a messy bed, draws and a cupboard. The smell of cigarette smoke lingers, someone has been here recently...")
Bathroom = Room("You are in a bathroom.  It reeks of mould There is a pile of dirty washing, toilet, basin and shower")
Office = Room("You are in an office. There is a desk with a laptop on it, a book shelf and a large painting that looks out of place")
Secret_Room = Room("You are in a secret room. There is a metal medical table with a vast array of medical tools on it. There is also a desk with security monitors up the front.")
###################################
#DEFINE CONNECTIONS
###################################

Lounge.south = Hallway
Lounge.east = Dining_Room
Dining_Room.east = Kitchen
Dining_Room.south = Office
Office.east = Secret_Room
Office.west = Hallway
Hallway.south = Bathroom
Hallway.west = Bedroom2

###################################
#DEFINE ITEMS
###################################
Item.description = ""
Broken_Draw_Handle = Item("draw handle","broken draw handle","handle")
Newspaper1 = Item("")
Documents = Item("")
Gun = Item("")
Secret_Room_Key = Item("")
Safe_Receipt = Item("")
Remote = Item("")
Scalpel = Item("")
Safe_Code = Item("")
Security_System_Papers = Item("")
House_Layout = Item("")
Laptop = Item("")
Beer = Item("")
Security_Monitors = Item("")
Paperclip = Item("paperclip","Paperclip")
Coin = Item("coin")

###################################
#DEFINE BAGS
###################################
inventory = Bag()
Room.items = Bag()

###################################
#ADD ITEMS TO BAG
###################################



###################################
#DEFINE ANY VARIABLES
###################################
current_room = Bedroom1
wakeup = False
found_paperclip = False
handcuff_locked = True
Bedroom1_escape = False
draw_handle_unscrewed = False
move_bed = False



###################################
#BINDS
###################################

if wakeup == False and current_room == Bedroom1:
	wakeup == True
	print("You wake up with a piercing headache...") 
	time.sleep(3)
	print("You try to stretch your arms but something holds them back. Startled you look and see that your right hand is handcuffed to a bedframe.")
	time.sleep(6)
	print(f"Your mind races and thinks about the night before. You were at a party...")
	time.sleep(2.5)
	print("and you...")
	time.sleep(1)
	print("you...")
	time.sleep(0.75)
	print("damn!")
	time.sleep(1) 
	print("You don't remember a single thing.")
	time.sleep(2)
	while found_paperclip == False:
		time.sleep(1)
		beginning_choice = input("What should you do?\n[1] Search Pockets, [2] Shout for help, [3] Struggle\n\n> ")
		if beginning_choice == "1":
			print("You empty your pockets and out falls a paper clip and a coin.\n")
			found_paperclip = True
			Bedroom1.items.add(Paperclip)
			Bedroom1.items.add(Coin)
		elif beginning_choice == "2":
			print("You shout for help but there's no replies...\n")
		elif beginning_choice == "3":
			print("You struggle to free your hand from the handcuff but you only tire yourself out.\n")
		else:
			print(f"I don't understand '{beginning_choice}'\n")

if Bedroom1_escape == True:
	Bedroom1.east = Lounge

@when("pick lock")
@when("pick cuff")
@when("pick handcuff")
@when("use paperclip")
def pick_lock():
	global handcuff_locked
	if "paperclip" in inventory and handcuff_locked == True:
		print("You mold the paperclip into a makeshift key. From your knowledge handcuffs have very simple locks.")
		time.sleep(1)
		print("After a few twists and turns the handcuffs fall off and you can now freely move around the room")
		handcuff_locked = False
	elif handcuff_locked == False:
		print("You have already used paperclip")
	else:
		print("You don't have a paperclip")

@when("look at cupboard")
@when("explore cupboard")
@when("go to cupboard")
def cupboard():
	global handcuff_locked
	if handcuff_locked == False:
		print("You walk over to the cupboard and open it. There's nothing in there except a few cobwebs")
	else:
		print("You can't do that when you are handcuffed")

@when("go to draws")
@when("look at draws")
@when("explore draws")
def draws():
	global handcuff_locked
	global draw_handle_unscrewed
	if handcuff_locked == False and draw_handle_unscrewed == False:
		print("You walk over to the draws and open them. There's nothing inside them however one handle broken and is being held on by one flathead screw.")
		@when("use coin")
		@when("unscrew screw")
		@when("unscrew flathead screw")
		def unscrew_handle():
			global draw_handle_unscrewed
			if "coin" in inventory and draw_handle_unscrewed == False:
				draw_handle_unscrewed = True 
				print("You unscrew the draw handle and it falls to the ground.")
				current_room.items.add(Broken_Draw_Handle)
			elif draw_handle_unscrewed == True:
				print("You have already used coin")
			else:
				print("You don't have 'coin' in your inventory")
	elif handcuff_locked == False and draw_handle_unscrewed == True:
		print("You walk over to the draws and open them. There's nothing inside them")
	else:
		print("You can't do that when you are handcuffed")

@when("go to bed")
@when("look at bed")
@when("explore bed")
def bed():
	global handcuff_locked
	global move_bed
	if handcuff_locked == False and move_bed == False:
		print("You go over to the bed. It has white sheets, a pillow and seems to be moveable.")
		@when("move bed")
		def move_bed():
			global move_bed
			move_bed = True
			print("You move the bed and reveal a vent.")
	elif move_bed == True:
		print("You go over to the bed. It has white sheet, a pillow and there is a vent to the side of it.")
	else:
		print("You can't do that when you are handcuffed")

@when("inventory")
def check_inventory():
	print("you are carrying:")
	for item in inventory:
		print(item)

@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def get_item(item):
	#check if item is in room
	#take item out of room
	#put it in inventory
	#otherwise tell user there is no item
	if item in current_room.items:
		print(f"You pick up the {item}")
		t = current_room.items.take(item)
		inventory.add(t)
	else:
		print(f"You don't see a {item}")

@when("go DIRECTION")
@when("travel DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		#checks if the current room list of exits had the direction the player wants to go
		current_room = current_room.exit(direction)
		print(f"You go {direction}")
		print(current_room)
	else:
		print("You can't go that way")

@when("look")
@when("explore room")
def look():
	global current_room
	print(current_room)
	exits_amount = int(len(current_room.exits()))
	if exits_amount == 1:
		#grammatically correct way of saying there is one exit
		print(f"There is a visible exit to the {', '.join(current_room.exits())}")
	elif exits_amount > 1:
		#grammatically correct way of saying there is more than one exit
		print(f"There are visible exits to the {', '.join(current_room.exits()[:-1]) + ' and ' + current_room.exits()[-1]}")
	else:
		print("There are no visible exits")




###################################
#MAIN FUNCTION
###################################
def main():
	start()
	#start the main loop

main()


