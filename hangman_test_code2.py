import string
import hangman_lib

secret_word = hangman_lib.get_random_word()
letters_guessed = []
mistakes_made = 0

#definitions
MAX_MISTAKES = 6

## def helper_functions
def word_guessed():
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

	print string.join(list_of_letters, '')


print "Lets start playing"
print "Are You Ready.."

print "Press [ENTER] to get started."
raw_input()
print "The Secret Word has length", len(secret_word)

hangman_lib.print_hangman_image(0)
while mistakes_made<MAX_MISTAKES:
	print "Word guessed So far", print_guessed()

	guess = string.lower(raw_input("Guess a letter"))

	letters_guessed.append(guess)
	if guess in secret_word:
		print "Good Guess"

		if word_guessed():
			print "Job Done. You Win"
			break

	else:
		print "Sorry, Hard Luck"
		print "Chances Left:", MAX_MISTAKES-mistakes_made
		mistakes_made+=1
		hangman_lib.print_hangman_image(mistakes_made)


if mistakes_made>=MAX_MISTAKES:
	print "You Lose"
	print "The word was: ", secret_word
else:
	print "Congrats"
	print "You correctly guessed:", secret_word
