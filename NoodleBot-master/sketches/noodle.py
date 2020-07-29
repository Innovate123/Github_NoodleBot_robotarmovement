#define the portion for each ingredient
no = 0
littleBit = 1
normal = 2
more = 3

# define constant for sauce
abaloneSauce = 11
chilliSauce = 12
tomatoSauce = 13
porkLard = 14
mushroomBroth = 15

# define constant for Condiment
lettuce = 21
mincedPork = 22
springOnion = 23
abaloneStick = 24
fishBall = 25

# define constant for type of noodles
meePok = 31
meeKia = 32
kuayTeow = 33

# define constant for type of bowl (dry or soup)
dry = 41
soup = 42


class Sauce():
	
	def __init__(self, sauceType, need):
		self.sauceTypeId = sauceType
		self.needToPut = need

class Condiment():
	
	def __init__(self, condimentType, need):
		self.condimentTypeId = condimentType
		self.needToPut = need
		
class NoodleType():
	
	def __init__(self, noodleType, size):
		self.noodleType = noodleType
		self.size = size

class Noodle():
	
	def __init__(self, noodle, bowlType, sauceList, condimentList):
		self.noodle = noodle
		self.bowlType = bowlType
		self.listOfSource = sauceList# define constant for sauce
		self.listOfCondiment = condimentList
		
	def print(self):
		return self.noodle
		

# Order 1 noodles

noodle = NoodleType(meePok, normal)
bowl = dry

listOfSauce = []
listOfSauce.append(Sauce(abaloneSauce, no))
listOfSauce.append(Sauce(chilliSauce, normal))
listOfSauce.append(Sauce(tomatoSauce, normal))
listOfSauce.append(Sauce(porkLard, normal))
listOfSauce.append(Sauce(mushroomBroth, normal))

listOfCondiments = []
listOfCondiments.append(Condiment(lettuce, normal))
listOfCondiments.append(Condiment(mincedPork, normal))
listOfCondiments.append(Condiment(springOnion, normal))
listOfCondiments.append(Condiment(abaloneStick, no))
listOfCondiments.append(Condiment(fishBall, normal))

myNoodle = Noodle(noodle, bowl, listOfSauce, listOfCondiments)

# Simulate the robot via output infromation
print(myNoodle.noodle.noodleType)
print(myNoodle.bowlType)
for sauce in myNoodle.listOfSource:
	print(sauce.sauceTypeId, sauce.needToPut)
	
for condiment in myNoodle.listOfCondiment:
	print(condiment.condimentTypeId, condiment.needToPut)