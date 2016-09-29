
import random

# Create a list of possible answers
Sharks = ["TIGER", "GREAT WHITE", "HAMMERHEAD", "NURSE", "MAKO", "BULL", "BLUE","BASKING", "WHALE", "SAND", "LEMON", "THRESHER", "BLACKTIP", "WHITETIP","REQUIEM" ]

# The program will choose a random item from the list
answer = random.choice(Sharks)

jumble = list(answer)


# Scramble the letters in jumble (mix them up)
for current_index in range(len(jumble)):    # Loop through all the letters
    random_index = random.randrange(0, len(jumble))
    # Swap the letters at that position
    temp = jumble[current_index]    # Remember the value at the current index
    jumble[current_index] = jumble[random_index]
    jumble[random_index] = temp

# print (jumble)
print ("Welcome to Word Jumble!\n")
for letter in jumble:
    print letter,


while True:
    guess = raw_input("\n\nWhat kind of shark is jumbled?: ")
    guess = guess.upper()
    if guess == answer:
        print ("You win")
        break
    else:
        print ("Try Again")
        continue
