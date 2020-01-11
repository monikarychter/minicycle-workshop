

player = {
    'room': 'outside',
}

rooms = {
    "outside": {
        "title": "Outside",
        "description": "You are standing outside of a huge cave entrance on the East. Up North there is a ladder",
    },
    "cave": {
        "title": "Cave",
        "description": "You're in a cave.",
    },
    "heaven":{
        "title": "Heaven",
        "description": "You see GOD. Wow"
    }
}


def main():
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
           player['room']= 'cave'
           describe_room()
        elif command in ["North", 'n']:
            player['room']= 'heaven'
            describe_room()
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
