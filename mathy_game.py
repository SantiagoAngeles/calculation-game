import random


def run():

	menu = """
	1 - Addition				3 - Addtion and substraction
	2 - Subtraction				4 - Equations 1 *
	____________________________________________________________________
	
	5 - Product				7 - Product and quotient *
	6 - Quotient				8 - Equations 2 *
	____________________________________________________________________
	*
	9 - Odd numbers				11 - Operations and percentages
	10 - Percentages			12 - Equations 3
	____________________________________________________________________

	13 - Matrices *
	20 - Quit *


	"""

	menu_opt = (input(menu))

	while True:
		if menu_opt == "1":
			addtion()
		elif menu_opt == "2":
			substaction()
		elif menu_opt == "3":
			mixed_as()
		elif menu_opt == "5":
			product()
		elif menu_opt == "6":
			quotient()
		elif menu_opt == "7":
			pass

		else:
			print("Type a valid option please :/")
			
			return False
		
		continue


def addtion():
	
	fnumber = random.randint(1, 1000)
	snumber = random.randint(1, 1000)
	tnumber = random.randint(1, 100)

	print(" ")
	
	print("			" + str(fnumber) + " + " + str(snumber) + " + " + str(tnumber) + " = " + "?")

	print(" ")
	
	answer = int(fnumber + snumber + tnumber)
	user = int(input("     Type your answer =  "))


	while user != answer:
		user = int(input("Here's another chance =  "))

	if user == answer:
		print("						    Correct!, here you go")
		print("     ____________________________________________________________________")

	else:
		pass
			

def substaction():

	fnumber = random.randint(1, 100)
	snumber = random.randint(1, 100)
	tnumber = random.randint(1, 100)


	print(" ")
	
	print("			" + str(fnumber) + " - " + str(snumber) + " - " + str(tnumber) + " = " + "?")

	print(" ")
	
	answer = int(fnumber - snumber - tnumber)
	user = int(input("     Type your answer =  "))


	while user != answer:
		user = int(input("Here's another chance = "))

	if user == answer:
			print("						    Correct!, here you go")
			print("     ____________________________________________________________________")

	else:
		pass

def mixed_as():
	
	fnumber = random.randint(-100, 100)
	snumber = random.randint(-100, 100)
	tnumber = random.randint(-100, 100)

#	count = 0

	print(" ")
	
	print("				" + str(fnumber) + " + " + str(snumber) + " + " + str(tnumber) + " =")

	print(" ")
	
#	count += 1

	answer = (fnumber + snumber + tnumber)
	user = int(input("     Type your answer =  "))

#	user = [int(input("Write your anwswer: ")), "q"]

	while user != answer:
		user = int(input("Here's another chance =  "))

	if user == answer:
		print("						    Correct!, here you go")
		print("     ____________________________________________________________________")


#	elif user == user[1]:
#		print(count)

	else:
		pass


def product():
	
	fnumber = random.randint(-12, 12)
	snumber = random.randint(-12, 12)
	tnumber = random.randint(-12, 12)

	fnumber != 0
	fnumber != 0
	fnumber != 0

#	count = 0

	print(" ")
	
	print("				    " + str(fnumber) + " * " + str(snumber) + " * " + str(tnumber))

	print(" ")
	
#	count += 1

	answer = (fnumber * snumber * tnumber)
	user = int(input("     Type your answer =  "))

#	user = [int(input("Write your anwswer: ")), "q"]

	while user != answer:
		user = int(input("     Let's try again  =  "))

	if user == answer:
		print("						    Correct!, here you go")
		print("     ____________________________________________________________________")

#	elif user == user[1]:
#		print(count)

	else:
		pass


def quotient():
	
	fnumber = random.randint(-100, 100)
	#snumber = random.randint(-5, 5)

	snumber = 5

	#tnumber = random.randint(-100, 100)

#	count = 0

	print(" ")
	
	print("				    " + str(fnumber) + " / " + str(snumber)) #+ " / " + str(tnumber))

	print(" ")
	
#	count += 1

	answer = (fnumber // snumber) #/ tnumber)
	user = float(input("     Type your answer =  "))

#	user = [int(input("Write your anwswer: ")), "q"]

	while user != answer:
		user = float(input("     Let's try again  =  "))

	if user == answer:
		print("						    Correct!, here you go")
		print("     ____________________________________________________________________")

#	elif user == user[1]:
#		print(count)

	else:
		pass


# HERE'S CODE TO IMPLEMENT A MENU TO KEEP PRACTICING OR JUST QUIT
#			run()
#			question = ["y", "n"]
#			question = str(input(" Do you want to repeat? (Press y or n):  "))
#			if question == "y":
#				menu_opt == (input("1"))
#				run()

# HERE'S HOW TO GET OFF THE GAME ONCE ONE IS DONE
#		elif user == str(user):
#			break

		
#			else:
#				run()
#				menu_opt = "5"
	
# Here it would need to get a function to invoque just "+"

# THIS IS THE MENU OPTION 2
#	elif menu_opt == "2":
#		
#		fnumber = random.randint(1, 100)
#		snumber = random.randint(1, 100)
#		
#		
#		print("			" + str(fnumber) + " - " + str(snumber))
#
#		answer = int(fnumber - snumber)
#		user = int(input("	Your answer: "))
#
#		while user != answer:
#			user = int(input("Here's another chance: "))
#
#		if user == answer:
#			print("Correct, here you go!")
#			run()
#	
#	else:
#		pass
		
if __name__ == '__main__':
	run()
