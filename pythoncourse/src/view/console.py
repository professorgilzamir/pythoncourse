import model

def menu():
	print("**********************************\n"
		   "Selecione uma opção: \n"
		   "1 - Sincronizar Dados \n"
		   "2 - Buscar Unidade de Saúde \n"
		   "3 - Mostrar Todas as Unidade \n"
		   "4 - Sair \n"
		   "**********************************")

def userOption():
	return int(input(">> "))

def getLongitude():
	return float(input("Longitude: "))

def getLatitude():
	return float(input("Latitude: "))

def show(unSaude):
	print("---------INICIO>RESULTADO-----------------------------")
	if unSaude:
		print("Unidade de saúde encontrada: " + unSaude.nome)
	else:
		print("Unidade de saúde não encontrada")
	print("----------FIM>>>>RESULTADO----------------------------")
	
def showAll(listaDeUnidades):
	print("---------INICIO>RESULTADO-----------------------------")
	if (listaDeUnidades):
		for un in listaDeUnidades:
			show(un)
	else:
		print ("Nenhum resultado foi encontrado")
	print("----------FIM>>>>RESULTADO----------------------------")