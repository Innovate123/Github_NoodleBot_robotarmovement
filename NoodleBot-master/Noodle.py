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
		self.listOfSauce = sauceList
		self.listOfCondiment = condimentList
		
	#def print(self):
	#	return self.noodle
		