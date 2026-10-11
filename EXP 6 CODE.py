
def vacuum_cleaner():
    room = {'A': 1, 'B': 1}
    position = 'A'

    while 0 in room.values():
        if room[position] == 0:
            print(position, "is dirty. Cleaning...")
            room[position] = 1
        else:
            print(position, "is clean.")

        if position == 'A':
            position = 'B'
        else:
            position = 'A'

    print("Both rooms are clean!")

vacuum_cleaner()
