import random	#to chose a random word from a list
ALPHABET = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
LIST_OF_WORDS = [] 														#to have many words in the game
with open('list_of_noun.txt') as word_to_guess:
	for line in word_to_guess:
		line = line.rstrip()
		LIST_OF_WORDS.append(line)

NUMBER_OF_ATTEMPTS = 10												#can be changed if we want longer play
start = input('Enter Y if you want to start the game: ')
# Little function to translate the Word in to the list
def list_maker(word):
	word_to_list = []
	for i in word:
		word_to_list.append(i)
	return word_to_list

#Main body of the game code

if str(start) == 'Y':
	secret_word = LIST_OF_WORDS[random.randint(0,len(LIST_OF_WORDS)-1)]   #to chose a random word
	print("The word has ", len(secret_word), 'letters!')
	secret_word_list = list_maker(secret_word)
	player_view = []                                                      #List to storage the guessed letters to the player
	wrong_letters = []													  #Storage to represent the wrong letters to the player
	for i in secret_word:												  #The way to represent the guessed letters to the player
		player_view.append('_')
	print(player_view)
	num_wrong = 0
	# THE GAME of HangedMan 

	while player_view != secret_word_list and num_wrong != NUMBER_OF_ATTEMPTS:
		print('You have, ' + str(NUMBER_OF_ATTEMPTS-num_wrong) + ' attempts, chose your letter wisely!')
		letter_from_player = input("Enter a letter: ")
		# Pack the inndices of the correct letters in to the list
		if letter_from_player.lower() in ALPHABET:							#Sentinel for wrong input
			if letter_from_player in secret_word_list and letter_from_player not in player_view:
				indices = [index for index, element in enumerate(secret_word_list) if element == letter_from_player]
				# Add correct letters to the player_view to represent the progress
				for index in indices:
					player_view[index] = letter_from_player
				print('This is correct letter!')
				print(player_view)
			

			elif letter_from_player in player_view: # Check if the letter already played
				print('You already guessed this letter')
				print(player_view)
				
			elif letter_from_player in wrong_letters: # Check if the letter already played
				print('You already tried this one')
				print(wrong_letters)
				
			elif num_wrong != (NUMBER_OF_ATTEMPTS-1): # Case of wrong letter
				num_wrong +=1
				wrong_letters.append(letter_from_player)
				print('This is wrong letter :( ')
				#print("You still have ", str(NUMBER_OF_ATTEMPTS-num_wrong), 'attempts.')
				print('Try another letter.')
			else: # Last case of wrong letter
				num_wrong +=1
				print('This was your last wrong letter :(')
		else:
			print('Please use only letters from english alphabet')


	if num_wrong == NUMBER_OF_ATTEMPTS:
		print('Sorry, you hanged! (x_x)')
		print('The correct word is ', secret_word)
	else:
		print("CONGRATULATIONS, YOU WIN! We won't hang you today =*")
else:
	print('Than why do you come here?')

		



