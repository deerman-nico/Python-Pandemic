class Person:
	def __init__(self,S, I, R, carrier, Student, age,  Infection_date):
		self.S = S
		self.I = I
		self.R = R
		self.carrier =  carrier
		self.Student = Student
		self.age = age
		self.Infection_date =  Infection_date

	def sickify(self):
		if self.S == True:
			self.S = False
			self.I = True
			self.R = False
		if self.I == True:
			self.S = False
			self.I = True
			self.R = False
		if self.R == True:
			self.S = False
			self.I = False
			self.R = True
		if self.carrier == True:
			self.S = False
			self.I = True 
			self.R = False
			self.carrier = False

	def infectify(self):
		if self.I == True or self.R == True:
			pass

		else:
			self.S = False
			self.I = False
			self.R = False
			self.carrier = True

	def recover(self):
		self.S = False
		self.I = False
		self.R = True
		self.carrier = False

	def studentify(self):
		self.Student = True

	def status(self):
		if self.S == True:
			return "Susceptible"
		elif self.I == True:
			return "Infected"
		elif self.R == True:
			return "Recovered"
		elif self.carrier == True:
			return "carrier"

	def status_update(self, day):
		self.age = day
		if self.carrier == True:
			self.Infection_date = day
			self.sickify()
		if (self.age - self.Infection_date) >= 14:
			self.recover()

class Building:
	def __init__(self):
		self.room = []

	def insert(self, Person):
		self.room.append(Person)









