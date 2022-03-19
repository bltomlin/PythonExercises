# read animals.txt
# and write animals_new.txt
animals = open('animals.txt', 'r', encoding="utf-8")
list_animals = animals.readlines()
animals.close()
animals_new = open('animals_new.txt', 'w', encoding="utf-8")
for animal in list_animals:
    animals_new.write(animal.replace('\n', ' '))
animals_new.close()
