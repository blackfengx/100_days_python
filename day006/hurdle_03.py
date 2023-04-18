# Link to website
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


def hurdle():
    # turn_left()
    # move()
    # turn_right()
    # move()
    # turn_right()
    # move()
    # turn_left()

def turn_right():
    # turn_left()
    # turn_left()
    # turn_left()

def jump_check():
    # while not front_is_clear():
        hurdle()

jump_check()

# while front_is_clear():
#     if not at_goal():
#         move()
#         jump_check()
#     if at_goal():
#         done()


# //////////////////////////////////////////////////////////////////
# Better Solution

#while not at_goal():
    #if wall_in_front():
        #hurdle():
    #else:
        #move()
