"""
Let's say you have a dictionary matching your friends' names with their favorite flowers:

fav_flowers = {'Alex': 'field flowers', 'Kate': 'daffodil', 'Eva': 'artichoke flower', 'Daniel': 'tulip'}
Your new friend Alice likes orchid the most: add this info to the fav_flowers dict and print the dict.

NB: Do not redefine the dictionary itself, just add the new element to the existing one.
"""

favorite_flowers = dict({'Alex': 'field flowers', 
                         'Kate': 'daffodil', 
                         'Eva': 'artichoke flower', 
                         'Daniel': 'tulip'}, Alice='orchid')
print(favorite_flowers)
