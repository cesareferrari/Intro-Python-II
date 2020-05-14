from room import Room
from player import Player

directions = ("n", "s", "e", "w")

# Declare all the rooms

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("My Player", rooms['outside'])

selection = None

# Write a loop that:
# while True

# If the user enters "q", quit the game.
while selection != 'q':
    # * Prints the current room name
    print("Current room:", player.current_room.name)

    # * Prints the current description
    # (the textwrap module might be useful here).
    print(player.current_room.description)

    # * Waits for user input and decides what to do.
    selection = input("Enter [n, s, e, w] to play or [q] to quit: ")
    print("Your selection was: ", selection)

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if selection in directions:
        if selection == "n":
            player.current_room = player.current_room.n_to
        if selection == "s":
            player.current_room = player.current_room.s_to
        if selection == "e":
            player.current_room = player.current_room.e_to
        if selection == "w":
            player.current_room = player.current_room.w_to
    elif selection == 'q':
        print("Quitting the game. Thanks for playing.")
    else:
        print("Must enter: [n, s, e, w]")



"""
directions = {'n': 'n_to', 's': 's_to', ...}
direction = directions[choice]

try:
    player.current_room = getattr(player.current_room, direction)

except AttribueError:
    print("You can't go that way")


hasattr(thing, attribute) ???

"""
