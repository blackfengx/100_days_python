# This code solves a hurdle problem that randomly generates hurdle height and goal placement. Further info at
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# MY SOLUTION ///////////////////

# def hurdle():
#     while wall_on_right():
#         if at_goal():
#             done()
#         if wall_in_front():
#             turn_left()
#         move()
#     else:
#         turn_right()
#         move()
#         turn_right()
#         move()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if not wall_in_front():
#         if at_goal():
#             done()
#         move()
#     if wall_in_front():
#         turn_left()
#         if at_goal():
#             done()
#         if not wall_in_front():
#             hurdle()

# Other Solution //////////////////

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right
#     while front_is_clear():
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else():
#         move()
