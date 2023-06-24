import random


def run():

	menu = """
	1 - Addition
	2 - Subtraction
	3 - Addtion and substraction
	
	4 - Product
	5 - Quotient *
	6 - Product and quotient *

	7 - Mixed all *

	8 - Quit *

	* = (not available yet)
	"""

	menu_opt = (input(menu))

	while True:
		if menu_opt == "1":
			addtion()
		elif menu_opt == "2":
			substaction()
		elif menu_opt == "3":
			mixed_as()
		elif menu_opt == "4":
			product()

		else:
			print("Type a valid option please :/")
			
			return False
		
		continue


def addtion():
	
	fnumber = random.randint(1, 100)
	snumber = random.randint(1, 100)
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
	
	fnumber = random.randint(-10, 10)
	snumber = random.randint(-10, 10)
	tnumber = random.randint(-10, 10)

#	count = 0

	print(" ")
	
	print("				" + str(fnumber) + " * " + str(snumber) + " * " + str(tnumber) + " =")

	print(" ")
	
#	count += 1

	answer = (fnumber * snumber * tnumber)
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
