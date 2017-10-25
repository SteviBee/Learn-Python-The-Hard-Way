from random import randint

class Archery(object):

    def enter(self):
        print "You are a brave, young, competitor in a medieval battle of life and death."
        print "You will have tests, trials, and challenges to face and if you are lucky"
        print "then maybe you can get out alive. You journey starts at the archery range."
        print "You come to an archery range where you must prove your accuracy."
        print "You have three arrows and need to score 15 points to advance."
        print "Aim for the 'outer ring' (5 pts.), 'middle ring' (10 pts.) or 'bullseye' (25 pts.)"
        print "Good luck! \n \n"

        counter = 0
        score = 0
        while counter < 3:

            aim = raw_input("What target do you want to aim at? ")

            if aim == 'outer ring':
                x = randint(1,2)
                y = randint(1,2)
                counter += 1
                if x == y:
                    print "Hit! You just got 5 pts.!"
                    score += 5
                else:
                    print "You missed :("
                    pass
                print "Your score is now:, ", score

            elif aim == 'middle ring':
                x = randint(1,3)
                y = randint(1,3)
                counter += 1
                if x == y:
                    print "Hit! You just got 10 pts.!"
                    score += 10
                else:
                    print "You missed :("
                    pass
                print "Your score is now:, ", score

            elif aim == 'bullseye':
                x = randint(1,4)
                y = randint(1,4)
                counter += 1
                if x == y:
                    print "Hit! You just got 25 pts.!"
                    score += 25
                else:
                    print "You missed :("
                    pass
                print "Your score is now:, ", score

            else:
                print "Does not compute!"
                return 'archery'

        if score >= 15:
            print "\n \n"
            print "Your aim is the truest around. There has never been a better archer."
            print "You beat all the others at the archery contest and leave the range"
            print "and head to the next event. "
            return "sword_fight"
        else:
            print "\n \n"
            print "You didn't score enough points to advance to the next round"
            print "Your shame overwhelms you and in your desparate state your immune system weakens."
            print "You catch the plage and never recover."
            return "die"
