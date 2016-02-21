def main_street_1():
	print "You are on Main Street!"  
	print "Sleeping Beauty's Castle is straight down and City Hall is to the left."
	print "Go straight or turn left?"
	choice = raw_input("> ")
	
	if "straight" in choice:
		main_street_2()
	if "left" in choice:
		#todo make city_hall
		city_hall()
	else:
		main_street_1()
		
def main_street_2():
	print "You continue down Main Street."
	print "You see Mickey in a battle with Captain Hook next to the clock shop."
	print "It looks like Mickey needs help distracting Captain Hook."
	print "What do you do?"
	while True:
		choice = raw_input("> ")
		if "clock" in choice:
			print "Tick Tock! Tick Tock!"
			print "Captain Hook eyes widen as he looks for the running clock."
			print "His skin goes ghostly white and he freezes."
			print "Mickey acts quick, and ties a rope around Hook's feet."
			print "Mickey says, \"Golly! Thanks for the help!\" and runs toward the castle."
			main_street_3()

def main_street_3():
	print "You see the castle straight ahead, the little red wagon on the right, and adventureland on the left."
	while True:
		choice = raw_input("> ")
		if ("wagon", "right") in choice:
			print "The wagon is closed today."
		
	
	
	
main_street_1()