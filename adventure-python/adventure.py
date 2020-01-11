
outside = {'e': 'cave', 'n': 'heaven', 's': 'hole', 'w': 'sea'}
cave = {'w':'outside', 'e':'east_corridor', 's': 'south_corridor'}
heaven = {'s': "outside", 'n': 'hell'}
str_dict = {'outside': outside, "cave": cave, "heaven": heaven}

player = {
    'room': 'outside',
}

rooms = {
    "outside": {
        "title": "Outside",
        "description": "You are standing outside of a huge cave entrance on the East. Up North is a ladder. South - hole, and West - sea",
    },
    "cave": {
        "title": "Cave",
        "description": "You're in a cave.",
    },
    "heaven":{
        "title": "Heaven",
        "description": "You see GOD. Wow"
    },
    "hole":{
        "title": "Hole",
        "description": "You see a huge hole"
    },
    "sea":{
        "title": "Sea",
        "description": "You see a boat"
    },
    "east_corridor":{
        "title": "East corridor",
        "description": "Height around 90 cm and wet wall"
    },
    "south_corridor":{
        "title": "South corridor",
        "description": "You see a bog"
    },
    "hell":{
        "title": "Hell",
        "description": "You see ass Piotra"
    }
}

def main():
    current_location = "outside"
    describe_room()
    playing = True
    while playing:
        command = get_command()
        if command in ['look', 'l']:
            describe_room()
        elif command in ['quit', 'q']:
            print('Bye!')
            playing = False
        elif command in ['East', 'e']:
           player['room']= str_dict[current_location]['e']
           describe_room()
           current_location = str_dict[current_location]['e']
        elif command in ["North", 'n']:
            player['room']= str_dict[current_location]['n']
            describe_room()
            current_location = str_dict[current_location]['n']
        elif command in ["South", 's']:
            player['room']= str_dict[current_location]['s']
            describe_room()
            current_location = str_dict[current_location]['s']
        elif command in ["West", 'w']:
            player['room']= str_dict[current_location]['w']
            describe_room()
            current_location = str_dict[current_location]['w']    
        else:
            print(f'Unrecognized command: {command}')


def get_command():
    print()
    return input('> ')


def describe_room():
    room = rooms[player['room']]
    print()
    print(room['title'])
    print()
    print(room['description'])


if __name__ == '__main__':
    main()
