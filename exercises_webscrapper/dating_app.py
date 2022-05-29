
#There's a list with info about people who search for a date. For each person, a few parameters are specified: their gender, age, hobbies, and city.

from operator import contains
from unicodedata import name
from xmlrpc.client import boolean


potential_dates = [{"name": "Julia", "gender": "female", "age": 29,
                    "hobbies": ["jogging", "music"], "city": "Hamburg"},
                   {"name": "Sasha", "gender": "male", "age": 18,
                    "hobbies": ["rock music", "art"], "city": "Berlin"}, 
                   {"name": "Maria", "gender": "female", "age": 35,
                    "hobbies": ["art"], "city": "Berlin"},
                   {"name": "Daniel", "gender": "non-conforming", "age": 50,
                    "hobbies": ["boxing", "reading", "art"], "city": "Berlin"}, 
                   {"name": "John", "gender": "male", "age": 41,
                    "hobbies": ["reading", "alpinism", "museums"], "city": "Munich"}]
#Help a new user write a function that selects from the given list people older than 30, interested in art, and living in Berlin. The function should return their names as a string, separated by a comma and a space, e.g. "Maria, Daniel" for the example list above.


def select_dates(potential_dates):
    name_list = []
    art_true = False
    for obj in potential_dates:
        for art in obj['hobbies']:
            if art == 'art':
                art_true = True
                if int(obj['age']) >= 30 and art_true ==True and obj['city'] == 'Berlin':
                    name_list.append(obj['name'])
    print(", ".join(name_list))

select_dates(potential_dates)