# Said Moussadeqimport randomdef generateNumber(1,topLimit)# Ask the player to guess 6 times. for guessesTaken in range(1, times+1):        print('Take your guess.’)
        guess = int(input())        if userGuess < userSecretNumber:	print(‘Your guess is too low.’)	return False        elif userGuess > userSecretNumber:	print(‘ Your guess is too high.’)	return False        else:            return True        if userGuess = userSecretNumber        print('Good job! You guessed my number!')    else:        print('Nope. The number I was thinking of was ' + str(userSecretNumber))