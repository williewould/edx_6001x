# _*_ utf-t _*_
# guess numbers
print('Please think of a number between 0 and 100!')
l=0
h=100
m=(l+h)/2
while True:
    print('Is your secret number ' + str(m))
    j=input("Enter 'h' to indicate the guess is too high." \
            "Enter 'l' to indicate the guess is too low." \
            "Enter 'c' to indicate I guessed correctly.")
    if j=='l':
        l=m
        m=(m+h)//2     
    elif j=='h':
        h=m
        m=(l+h)//2
    elif j=='c':
        print('Game over. Your secret number was: '+str(m))
        break
    else:
        print('Sorry, I did not understand your input.')
print("Please think of a number between 0 and 100!")
'''
# At the start the highest the number could be is 100 and the lowest is 0.
hi = 100
lo = 0
guessed = False

# Loop until we guess it correctly
while not guessed:
    # Bisection search: guess the midpoint between our current high and low guesses
    guess = (hi + lo)//2
    print("Is your secret number " + str(guess)+ "?")
    user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_inp == 'c':
        # We got it right!
        guessed = True
    elif user_inp == 'h':
        # Guess was too high. So make the current guess the highest possible guess.
        hi = guess
    elif user_inp == 'l':
        # Guess was too low. So make the current guess the lowest possible guess.
        lo = guess
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(guess))
'''
