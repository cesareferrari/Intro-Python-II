import random
import textwrap
from room import Room
from player import Player

directions = {"n": "n_to", "s": "s_to", "e": "e_to", "w": "w_to"}
allowed_directions = list(directions.keys())

# Text formatting and messages
# TODO: put into a module

wrapper = textwrap.TextWrapper(width=50) 

def print_yellow(skk):
    print("\033[93m{}\033[00m".format(skk))

def print_cyan(skk):
    print("\033[96m{}\033[00m".format(skk)) 

def print_red(skk):
    print("\033[91m{}\033[00m".format(skk)) 

selection_messages = [
        'You selected',
        'Mmmm... I see you chose',
        'Really? Did you choose',
        'Oh, my! You picked',
        'I don\'t know why you selected',
        ]


def try_enter_room(player, movement):
    if getattr(player.current_room, movement) is None:
        print_red("\nNope! Can't go there!")
    else:
        setattr(player, "current_room", getattr(player.current_room, movement))


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


# Main

# Make a new player object that is currently in the 'outside' room.
player = Player("Curly", rooms['outside'])

# Initial selection is None
selection = None

# Loop: If the user enters "q", quit the game.
while selection != 'q':
    # Print the current room name and description
    print_yellow(wrapper.fill(f"{player.name} is in '{player.current_room.name}'"))
    print_cyan(wrapper.fill(player.current_room.description))

    # Wait for user input and decide what to do.
    selection = input(f"Enter {allowed_directions} to play or ['q'] to quit: ")
    print(f"\n{random.choice(selection_messages)}", selection.upper())

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if selection in directions.keys():
        try_enter_room(player, directions[selection])
    elif selection == 'q':
        print("\nQuitting the game already? Thanks for playing.")
    else:
        print_red(f"\nWrong key! You should enter: {allowed_directions}")


