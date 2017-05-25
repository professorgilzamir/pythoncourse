from view import console as view
import model


def start():
	view.menu()
	opt = view.userOption()
	while (opt != 4):
		if opt == 1:
			model.syncdata()
		elif opt == 2:
			lo = view.getLongitude()
			la = view.getLatitude()
			unitHealth = model.searchNearUnitHealth(lo, la)
			view.show(unitHealth)
		elif opt == 3:
			listOfUnitHealth = model.searchAllUnitHealth()
			view.showAll(listOfUnitHealth)
		view.menu()
		opt = view.userOption()
	

