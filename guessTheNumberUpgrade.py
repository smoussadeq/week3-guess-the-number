# Said Moussadeqimport random
secretNumber = random.randint(1, 20)print(‘I am thinking of a number between 1 and 20.’)# Ask the player to guess 6 times. for guessesTaken in range(1, 7):        print('Take your guess #’ + str(guessesTaken+’:’)
        guess = int(input())        if userGuess < userSecretNumber:		print(‘Your guess is too low.’)		return False        elif userGuess > userSecretNumber:		print(‘ Your guess is too high.’)		return False        else:                return True

if( showAnswer == True):
  print(‘—shhh, the real number is’+str(theNumber)+’.’)        if userGuess = userSecretNumber        print('Good job! You guessed my number!')    else:        print('Nope. The number I was thinking of was ' + str(userSecretNumber))