#Create a file planets.txt and write the names of the Solar system planets there, each on a new line. In total, the file should contain 8 lines with the following planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.

planets = ['Mercury\n', 'Venus\n', 'Earth\n', 'Mars\n', 'Jupiter\n', 'Saturn\n', 'Uranus\n', 'Neptune\n']
new_file = open('planets.txt', 'a', encoding='utf-8')
new_file.writelines(planets)
new_file.close()