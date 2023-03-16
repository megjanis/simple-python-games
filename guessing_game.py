import random
guess = random.choice(open("nurseryrimes.py", "r").readline().split())
#print(random.choice(computer_guess))
character_count = len(guess)
#print("Guess the word:", end= "")
character_tracking = []
guess_limit = 10
underscores = 1
#out_of_guesses = False

while character_count:
    character_tracking.append("_")
    character_count = character_count - 1

    #print("_", end= "")


while underscores != 0 and guess_limit != 0:
    index = 0
    #print(len(computer_guess))
    print(character_tracking)
    print("You have " + str(guess_limit) + " guesses left." )

    user_guesses = input('\nPlease enter your guess: ')
    #print(user_guesses)
    flag = 0

    for elements in guess:
        #print(elements)

        if user_guesses == elements:

            print("Found it! ")

            flag = 1
            #character_tracking.insert(index,user_guesses)
            character_tracking[index] = user_guesses
            #computer_guess = computer_guess.replace(elements, "")

            #break

        index = index + 1
    underscores = 0
    for elements in character_tracking:
        if elements == "_":
            underscores = underscores + 1


    if flag != 1:
        guess_limit = guess_limit - 1
        print("Letter not found.Try again.")
if underscores == 0:
    print("Congratulations. You won the game!The word is: [ "+ guess + " ]")
else:
    print("You are out of guesses. Sorry, you lose.")

