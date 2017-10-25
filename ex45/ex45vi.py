print "You walk to the next and final event."
print "No competition is complete without a test of both strength and wit."
print "You see a board with an old man sitting accross from it."
print "He challenges you in a chess match. You must beat him to win."
print "Before you play you need to match the points you get for each chess piece."

dictofpieces = {
    "pawn":1,
    "knight":3,
    "bishop":3,
    "rook":5,
    "queen":9,
    }

score = 0
guesses = 1
while score <= 21 and guesses < 10:

    guesses += 1

    try:
        name = raw_input("What piece do you want to guess the value of? ")
        value = int(raw_input("What value do you think %s has? " % name))

        if value == dictofpieces[name]:
            print "You got a match!"
            score += dictofpieces[name]
            print "score = ", score
        else:
            print "try again"

    except (ValueError, KeyError) as error:
        print "Please enter a correct chess piece name"
        continue

if score >= 21:
    print "Congrats. You beat the chess master!"

else:
    print "You ran out of guesses. You are stoned to death."
