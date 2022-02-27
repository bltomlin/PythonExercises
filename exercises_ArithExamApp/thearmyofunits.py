#Write a program that will classify the army of your enemies

no_army = 1
few = range(1, 10)
pack = range(10, 50)
horde = range(50, 500)
swarm = range(500, 1000)

number_of_units = int(input())
if number_of_units < no_army:
    print('no army')
elif number_of_units in few:
    print('few')
elif number_of_units in pack:
    print('pack')
elif number_of_units in horde:
    print('horde')    
elif number_of_units in swarm:
    print('swarm')
else:
    print('legion')