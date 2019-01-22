directions = ['north','south','east','west']

# Data structure to store details of each location in the game
class Location:
    # Constructor - set up
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.linkedLocations = {}   # Empty dictionary - will store which locations are linked to which other locations

    def addLink(self, direction, destination):
        # Add link to linkedLocations dictionary (if the specified direction and destination are valid)
        if direction not in directions:
            raise ValueError('Invalid direction')
        elif destination not in locations:
            raise ValueError('Invalid destination')
        else:
            self.linkedLocations[direction] = destination

# Dictionary with location ID strings as keys and Location objects as the values
locations = { 'woods':Location('The woods', 'You are in the woods. There are lots of trees.'),
              'lake':Location('The lake', 'You are by the lake. It is very watery.') }

# Join the two locations together
locations['woods'].addLink('north','lake')
locations['lake'].addLink('south','woods')

# Player will start in the woods
currentLocation = locations['woods']

# Main game loop
while True:
    # Display description of current location
    print(currentLocation.description)

    # Display neighbouring locations
    for linkDirection,linkedLocation in currentLocation.linkedLocations.items():
        print(linkDirection + ': ' + locations[linkedLocation].name)

    # Read player input
    command = input('>').lower()
    if command in directions:
        if command not in currentLocation.linkedLocations:
            print('You cannot go that way')
        else:
            newLocationID = currentLocation.linkedLocations[command]
            currentLocation = locations[newLocationID]
    else:
        print('Try one of: ' + ', '.join(directions)) # Show list of directions, separated by commas
