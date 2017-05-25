import model

class View():
	def menu(self):
		print("**********************************\n"
			   "Selecione uma opção: \n"
			   "1 - Sincronizar Dados \n"
			   "2 - Buscar Unidade de Saúde \n"
			   "3 - Mostrar Todas as Unidade \n"
			   "4 - Sair \n"
			   "**********************************")

	def userOption(self):
		return int(input(">> "))

	def getLongitude(self):
		return float(input("Longitude: "))

	def getLatitude(self):
		return float(input("Latitude: "))

	def show(self, unSaude):
		print("---------INICIO>RESULTADO-----------------------------")
		if unSaude:
			print("Unidade de saúde encontrada: " + unSaude.nome)
		else:
			print("Unidade de saúde não encontrada")
		print("----------FIM>>>>RESULTADO----------------------------")

	def showAll(self, listaDeUnidades):
		print("---------INICIO>RESULTADO-----------------------------")
		if (listaDeUnidades):
			for un in listaDeUnidades:
				show(un)
		else:
			print ("Nenhum resultado foi encontrado")
		print("----------FIM>>>>RESULTADO----------------------------")

	def __init__(self):
		self.target = "console"