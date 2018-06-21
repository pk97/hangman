rom string import *
from hangman_lib import *

## Constants
MAX_MISTAKES = 6

#state variables

secret_word = get_random_word()
letters_guessed = []
mistakes_made = 0

##helper function...

def word_guessed():
	'''Returns True iff player has successfully guessed the word'''
	for letter in secret_word:
		if letter not in letters_guessed:
			return False

	return True

def print_guessed():
	list_of_letters = []
	for letter in secret_word:
		if letter in letters_guessed:
			list_of_letters.append(letter)
		else:
			list_of_letters.append('-')
	s = ''
	return s.join(list_of_letters)


##main game code
print ("Welcome To Hangman")

first_time = input("Is this your first time playing Hangman? (y/n)").lower()

if first_time=="y":
	print ("The objective of Hangman is to guess a secret word letter by letter.")
	print ("If you guess a letter in the word, we'll show you that letter.")
	print ("But if you guess wrong, we'll draw part of the hangman's body.")
	print ("Don't let his whole body get drawn, or else you lose!")

print ("Great, so you're ready to play. Just two things that might help:")
print ("1) The secret word has", len(secret_word), "letters.")
print ("2) It takes", MAX_MISTAKES, "wrong guesses to lose.")
print ()
print ("Good luck!")
print ()
print ("[Press enter when ready to play.]")
input()     # this just waits for them to press enter... they can type
                # other stuff but it doesn't affect anything.

print_hangman_image(0)

while mistakes_made<MAX_MISTAKES:

	print ("The word so far: ", print_guessed())
	print ("Letters guessed so far:")

	for letter in letters_guessed:
		print (letter)

	print ("Wrong guesses remaining:", MAX_MISTAKES-mistakes_made)

	guess = input("What letter will you guess").lower()

	if guess == "":
		print ("You have to guess something")

	elif len(guess)>1:
		print ("you can guess only one letter at a time.")

	elif guess in letters_guessed:
		print ("you have already guessed this!")

	else:
		letters_guessed.append(guess)

		if guess in secret_word:
			print ("Good Guess")

			if word_guessed():
				print ("You Done. Good Job")
				break
		else:
			mistakes_made =  mistakes_made+1
			print ("Sorry No luck")

			print_hangman_image(mistakes_made)

if mistakes_made>=MAX_MISTAKES:
	print ("On No, You Lose")
	print ("GAME OVER")
else:
	print ("Congrats")

print ("The word was: ",secret_word)
