from sys import exit
from random import randint
import shelve
import ex45v
#testing out uploading from cmd propmt

class Scene(object):
    """Parent class for all the scenes, all common attributes and properties go here."""

    def enter(self):
        """Run this, prints an error."""
        print "Not yet configured"
        exit(1)
        pass

class Engine(object):
    """Runs a map full of scenes.

    Attributes:
        scene_map: The first scene entered and executed
    """

    def __init__(self, scene_map):
        """inits Engine with self.scene_map = scene_map"""
        self.scene_map = scene_map

    def play(self):
        """executes the current_scene and keeps executing the next_scene.

        Starts a while loop and executes the enter function (which is part of
        every class) and then will change the current_scene to the instance of
        the returned string from the previous scene.
        """
        current_scene = self.scene_map.opening_scene()

        #this prvents people from entering wrong starting scene name
        if current_scene == 1:
            print "\nplease enter valid starting scene. Your options are:"
            del Map.scenes['win']
            print Map.scenes.keys() ,'\n'
            exit()
        else:
            pass

        while True:
            print "\n -------------------------------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Intro(object):
    """Gets Hero's information or recalls old player's info.

    Takes a yes/no raw input and either gathers or recalls players information
    depending on if they have used this program before. The two shelfs will be
    created if not already made.
    """
    def __init__(self):

        x = raw_input("Have you played this before? ").lower()

        if x == 'yes':
            # I have the variable of the name
            y = raw_input("What was your name? ").lower()
            # opening databases:
            s = shelve.open('speciality_shelf.db')
            e = shelve.open('enemey_shelf.db')
            try:
                self.name = y
                if y not in s:
                    print ("\nPlease enter valid Hero Name from before.\n")
                    exit()
            finally:
                s.close()
                e.close()

        else:
            self.info()
            # creates file if one doesn't exist
            s = shelve.open('speciality_shelf.db')
            e = shelve.open('enemey_shelf.db')
            try:
                s[self.name] = self.special
                e[self.name] = self.enemey
            finally:
                s.close()
                e.close()

    def info(self):
        """Takes user input and stores it in the respective shelf."""
        self.name = raw_input("What is your name? ").lower()
        while True:
                self.special = raw_input("What is your speciality: weapons, armor, or wisdom? ").lower()
                if self.special in ('weapons', 'armor', 'wisdom'):
                    break
                else:
                    print "PLEASE ENTER VALID SPECIALITY"
        else:
            pass
        self.enemey = raw_input("what is your enemey's name? ").lower()

# sets intro to the instance of class Intro()
intro = Intro()

# calling current variables and lists from the function info inside class intro
print "Hero's name: ", intro.name.title()
s = shelve.open('speciality_shelf.db')
e = shelve.open('enemey_shelf.db')
try:
    current_speciality = s.get(intro.name, "No data with that name available.")
    current_enemey = e.get(intro.name, "No data with that name available.")
finally:
    s.close()
    e.close()

# now i can use these variables to call the current special and enemeny whereever!
print "current speciality: ", current_speciality.title()
print "current enemey: ", current_enemey.title()

## =================================================================================

class Die(Scene):
    """The Death class is a scene that gives a funny way to die.

    Attributes:
        quips (list): A list of strings that is randomly printed.

    """

    quibs = [
        "You died. You suck.",
        "Your mom would not be proud",
        "Such a loser.",
        "I have a small child that's better at this."
    ]

    def enter(self):
        """Prints a random quib and closes the program"""
        print Die.quibs[randint(0, len(self.quibs)-1)]
        exit(1)

class Win(Scene):
    """Ends the program and prints out a Congrats statement."""

    def enter(self):
        """Ends the program and prints out a congrats string."""
        print "You Won! You beat everyone and survived the competition!"
        print "Congrats!!"
        exit()

class SwordFight(Scene):
    """Scene where you must enter the correct raw input to contiune."""

    def enter(self):
        """Takes user str input and returns next scene accordingly.

        Returns:
            die: If user fails to input correct response, which will
                        call Die scene and end program.
            chess_match: If user adances to next scene.
            DOES NOT COMPUTE: If wrong input from user.

        """
        print "You walk up to the next event. You see crowds of people surrounding"
        print "an arena. You hear metal clashing, screams, and broken things."
        print "You walk in and see the title of the next fight: \n"
        print "%s, the Black Knight vs. %s, the Newbie \n" % (current_enemey, intro.name)
        print "You are about to fight your biggest enemey in a sword fight!"
        print "Good luck!! \n \n"

        if current_speciality == "armor":
            print "You gain strength from your armor speciality"
            herohealth = 10
        else:
            herohealth = 5

        if current_speciality == "weapons":
            print "You gain attack from your weapons speciality"
            heroattack = 10
        else:
            heroattack = 5

        while True:

            print "You grab your sword and face off against %s." % current_enemey
            action = raw_input("What do you do? ")

            if action == "attack his head":
                print "The Black Knight is not phased by your attack."
                print "Actually it angers him and he crushes your face."
                return "die"

            elif action == "attack his body":
                print "You do some damage but it doesn't seem to phase him."
                print "He hits you back."
                if herohealth < 6:
                    return "die"
                else:
                    print "You survive his attack this time."
                    pass

            elif action == "duck":
                print "He is too fast for you and swings his weapon through your"
                print "gut and splits you into two!"
                return "die"

            elif action == "attack his arm":
                if heroattack > 6:
                    print "With your extra attack powers you cut through his armor"
                    print "and cut off his arm!"
                    print "He bleeds out and dies. Congrats!"
                    return "chess_match"
                else:
                    print "Your attack doesn't peirce his armor."
                    print "he swings back and guts you."
                    return "die"

            elif action == "attack his leg":
                print "You cut off his leg!"
                print "He stumbles and falls to the ground."
                x = raw_input("you can now finish him off. Do you 'kill' him or 'save' him? ")
                if x == "kill":
                    print "The crowd roars you stab him right in the heart!"
                    return "chess_match"
                else:
                    print "Empathy does not get you far here"
                    return "die"

            else:
                print "DOES NOT COMPUTE"
                pass

class ChessMatch(Scene):
    """Compares user input to a known dict."""

    def enter(self):
        """Compares user input to a known dict.

        Returns:
            die: If user fails to input correct response and ends program.
            win: If correct respones inputed.

        """
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

        if current_speciality == "wisdom":
            print "You gain wisdom from your wisdom speciality"
            score = 5
        else:
            score = 0

        guesses = 1

        while score <= 21 and guesses < 10:

            guesses += 1

            try:
                name = raw_input("What piece do you want to guess the value of? ")
                value = int(raw_input("What value do you think %s has? " % name))

                if value == dictofpieces[name]:
                    print "You got a match! and take one of the old man's pieces."
                    score += dictofpieces[name]
                    print "Total score = ", score
                else:
                    print "try again"

            except (ValueError, KeyError) as error:
                print "Please enter a correct chess piece name"
                continue

        if score >= 21:
            print "You guessed all the pieces, so you start your game."
            print "It is hard and challenging, but after hours of play"
            print "you come out on top of the old man with one final move!"
            print "Congrats! You beat the chess master!"
            return "win"
        else:
            print "You ran out of guesses. You are stoned to death."
            return "die"

## =================================================================================

class Map(object):
    """A class storing all the scenes we will use.

    Attributes:
        scenes (dict): Instatiates each scene when it is called for.

    """

        # creating a dict with strings calling the instance of each class
    scenes = {
        'archery': ex45v.Archery(),
        'sword_fight': SwordFight(),
        'chess_match': ChessMatch(),
        'win': Win(),
        'die': Die(),
        }

    def __init__(self, start_scene):
        """Sets the starting scene.

        Args:
            start_scene (str): Takes the starting class and passes it.

        """
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        """String we pass thru here returns the next scene (class) we want.

        Returns:

            value of key from scene (dict).

        """
        # use get method to return value (class) from scenes dict
        return Map.scenes.get(scene_name, 1)

    def opening_scene(self):
        """Sets the starting scene class."""
        return self.next_scene(self.start_scene)

a_map = Map(raw_input("Where do you want to start? Typically is 'archery' "))
a_game = Engine(a_map)
a_game.play()
