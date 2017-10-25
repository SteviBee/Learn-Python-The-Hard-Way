#i need this file to store all the profiles of people
def info():
    name = raw_input("What is your name? ")
    special = raw_input("What is your speciality: weapons, armor, or wisdom? ")
    enemey = raw_input("what is your enemey's name? ")

    x = "VARIABLE IN INFO (FUNCTION) INSIDE MODULE"

    #Ok, so you can use same key for mulitple values
    specialities = {name:special}
    enemeies = {name:enemey}

    #print profile
    print "Name: " , name
    #gives total profile (without name)
    #print "special & enemey? ",
    #i want to call just enemey
    print "should be just special %s, then just enemey %s." % (specialities[name], enemeies[name])
    return name, special, enemey, specialities, enemeies, x

#need to reference variable inside function from outside function
x = info()
print name
