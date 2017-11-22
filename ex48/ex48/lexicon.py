# from sys import argv ## don't know if i want it automated or not.
# script, *user_input = argv

direction = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verbs = ('go', 'stop',  'kill', 'eat')
stop_words = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')

def scan(x):
    raw_list_words = x.split()
    sentence = []

    for i in raw_list_words:

        if i in direction:
            sentence.append(("direction", i))
        elif i in verbs:
            sentence.append(("verb", i))
        elif i in stop_words:
            sentence.append(("stop", i))
        elif i in nouns:
            sentence.append(("noun", i))
        elif i.isdigit():
            try:
                sentence.append(("number", int(i)))
            except ValueError:
                    pass
        else:
            sentence.append(("error", i))

    return sentence

x = raw_input('> ').lower()
y = scan(x)
print y
