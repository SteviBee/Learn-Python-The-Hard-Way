class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

NW = Room("NW", "Short cut")
NW.add_paths({"NW": NW})
NW.go('NW')

newroom = Room('death', 'Where you go to die')
forward = newroom
back = newroom
jump = newroom
run = newroom

newroom.add_paths({'forward': forward, 'back': back, 'jump': jump, 'run': run})

x = newroom.go('forward')
print newroom.description
