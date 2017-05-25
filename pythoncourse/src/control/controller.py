from view import console as view
import model

class Controller():
	def start(self):
		self.view.menu()
		opt = self.view.userOption()
		while (opt != 4):
			if opt == 1:
				self.model.syncdata()
			elif opt == 2:
				lo = self.view.getLongitude()
				la = self.view.getLatitude()
				unitHealth = self.model.searchNearUnitHealth(lo, la)
				self.view.show(unitHealth)
			elif opt == 3:
				listOfUnitHealth = self.model.searchAllUnitHealth()
				self.view.showAll(listOfUnitHealth)
			self.view.menu()
			opt = self.view.userOption()
	
	def __init__(self):
		self.view = view.View()
		self.model = model.NetDataModel()
