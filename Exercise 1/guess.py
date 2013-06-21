import random

print "Howdy, what's your name?"
name = raw_input("> ")

print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name

compnumber = random.randint(1,100)
print compnumber

tries = 0

while True:
	tries += 1
	print "Your guess?",
	guess = int(raw_input("> "))

	if guess < 1 or guess > 100:
		print "Your guess must be between 1 and 100."

	elif guess != compnumber:
		if guess > compnumber:
			print "Your guess is too high, try again."
		else:
			print "Your guess is too low, try again."
	

	else:
		if tries == 1:
			print "Well done, %s! You found my number in 1 try!" % name
		else:
			print "Well done, %s! You found my number in %d tries!" % (name, tries)
		break


