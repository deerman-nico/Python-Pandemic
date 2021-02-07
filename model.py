import random
from random import randint
import classes
import matplotlib
import matplotlib.pyplot as plt

people = 1000
buildings = 350
days = 1000

school_lockdown = True
lockdown_start = 30
lockdown_end = 100
students = 500

death = True

people_per_building = people/ buildings
city = []
population = []

d = 1
p = 228

x = []
y_recover = []
y_infected = []
y_susceptible = []

patient0 = randint(0, people-1)
for i in range(0, people):
	population.append(classes.Person(True, False, False, False, False, 0, 1000))
population[patient0].sickify()
population[patient0].Infection_date = 0

if school_lockdown == True:
	for i in range(0, students):
		population[i].Student = True

random.shuffle(population)

for i in range(0, buildings):
	city.append(classes.Building())

for day in range(0, days):

	counter_s = 0
	counter_i = 0
	counter_r = 0

	for j in range(0, len(city)):
		for i in range(0, people_per_building):
			city[j].insert(population[0])
			population.pop(0)
	

	for i in range(0, buildings):
		for j in range(0, people_per_building):
			if school_lockdown == True and lockdown_end > day > lockdown_start and city[i].room[j].Student == True:
				continue
			else:
				if city[i].room[j].status() == "Infected":
					for y in city[i].room:
						c = randint(0, 1000)
						if p>=c:
							y.infectify()

	for j in range(0, len(city)):
		for i in range(0, people_per_building):
			population.append(city[j].room[0])
			city[j].room.pop(0)

	for i in population:
		i.status_update(day)
		if i.status() == "Susceptible":
			counter_s+=1
		if i.status() == "Infected":
			counter_i+=1
		if i.status() == "Recovered":
			counter_r+=1


	if death == True:
		for i in range(0, len(population)):
			d = randint(0, 100)
			if d <= 1:
				if population[i].Student == True:
					population.pop(i)
					population.append(classes.Person(True, False, False, False, True, 0, 1000))
				else:
					population.pop(i)
					population.append(classes.Person(True, False, False, False, False, 0, 1000))

	x.append(day)
	y_recover.append(counter_r)
	y_infected.append(counter_i)
	y_susceptible.append(counter_s)

	random.shuffle(population)

print("people:", people)
print( "buildings:", buildings)
print( "school_lockdown:", school_lockdown)
print("lockdown_start:", lockdown_start)
print("lockdown_end:", lockdown_end)
print("death:", death)

plt.plot(x, y_recover, "grey", label="recoveries")
plt.plot(x, y_infected, "-r", label="infections")
plt.plot(x, y_susceptible, "-b", label="susceptible")

plt.title("P:")
plt.xlabel("days")
plt.ylabel("people")

plt.legend(loc='best')

plt.show()







