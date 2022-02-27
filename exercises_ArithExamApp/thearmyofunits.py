#Write a program that will classify the army of your enemies

no_army = 1
few = range(1, 9)
pack = range(10, 99)
horde = range(100, 499)
swarm = range(500, 999)

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
