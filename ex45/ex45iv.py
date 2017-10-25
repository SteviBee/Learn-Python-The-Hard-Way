import shelve

#opening db via shelve
s = shelve.open('test_shelf.db')
try:
    #creating a new key:value relationship to dict 'test_shelf.dp'
    s['name'] = 'armor'
    s['other'] = 'weapon'
finally:
    print "printing the shelve: ", s
    s.close()


#now opening it, opens in r/w automatically otehr wise flag='r or w'
s = shelve.open('test_shelf.db')
try:
    #calling value from key reference and setting it equal to new variable
    new_value = s['name']
    other_value = s['other']

finally:
    s.close()

print "new value: ", new_value
print "other value: ", other_value
