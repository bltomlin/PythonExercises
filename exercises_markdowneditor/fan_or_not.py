"""
A bunch of friends got together to watch an esports tournament. Some of them have already decided on their favorite team and there are some who are interested in watching the competition only.

Your task is to implement the add_viewer() function:

    The function should take two arguments: a person's name and, optionally, the current fan_list (if a person does not have a favorite team yet, this argument should not be passed to the function).
    If the fan_list variable is passed to the function, the name of the person should be added to the providedfan_list, then this list should be returned.
    If the person is not a fan of any particular team, an empty list for non-fans should be created, the name of the person should be added there, and the list should be returned.

For example, if a string "Harry" and a list ["Mark", "Joshua"] are passed to the function, it should return the list ["Mark", "Joshua", "Harry"].

If a string "Molly" is passed to the function and the list is not, the function should return the list ["Molly"].

You do NOT need to handle input or call the function, just implement it.
"""


def add_viewer(name, fan_list=None):
    if fan_list is None:
        fan_list = []
    fan_list.append(name)
    return fan_list
