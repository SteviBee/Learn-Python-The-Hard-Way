from nose.tools import *
#from directory ex47 game module import Room class
from ex47.game import Room

#All of these create rooms and then makes sure the room works how it shoud work using assert.
#test out basic room features: name, definitions.
def test_room():
    gold = Room("GoldRoom", """This room has gold in it you can grab. There's a door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

#tests out basic room paths.
def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")
    east = Room("East", "Looking for the backdoor")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

#tests out whole map.
def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "it's dark down here, you can go up.")

    start.add_paths({'west' : west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
