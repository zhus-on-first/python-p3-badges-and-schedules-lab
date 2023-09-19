def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    # badges = []
    # for name in names:
    #     badges.append(f"Hello, my name is {name}.")
    
    badges = [f"Hello, my name is {name}." for name in names] 
    return badges

def assign_rooms(names):
    # rooms = []
    # for index in range(len(names)):
    #     rooms.append(f"Hello, {names[index]}! You'll be assigned to room {index + 1}!")

    rooms = [f"Hello, {names[index]}! You'll be assigned to room {index + 1}!" 
             for index in range(len(names))]
    return rooms


def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)

    # for badge in badges:
    #     print(badge)

    # for room in rooms:
    #     print(room)
    badges = [print(badge) for badge in badges]
    rooms = [print(room) for room in rooms]