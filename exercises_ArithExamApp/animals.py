# read animals.txt
# and write animals_new.txt
animals = open('animals.txt', 'r')
new_animals = open('new_animals.txt', 'w')
list_animals = animals.readlines()
for animal in list_animals:
    new_animals.write(animal.replace('\n', ' '))
new_animals.close()
animals.close()
