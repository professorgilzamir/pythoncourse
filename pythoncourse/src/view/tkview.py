from tkinter import *
import time
from threading import Thread
import atexit


class View():
	def __init__(self):
		self.userOpt = 0

		fontDestaque = ('Verdana', '13', 'bold')
		fontNormal = ('Verdana', '10', 'normal')

		self.root = Tk()
		self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

		self.reportFrame = Frame(self.root, pady=10)
		self.btReport = Button(self.reportFrame, text='Gerar relatório de unidades mais próximas')
		self.btReport['relief'] = RIDGE
		self.btReport['padx'], self.btReport['pady'] = 10, 5
		self.btReport['font'] = fontDestaque
		self.root.bind('')

		self.btReport.pack()
		self.reportFrame.pack()

		self.userInputFrame = Frame(self.root)

		self.lblInfCoords = Label(self.userInputFrame, 
			text='Informe suas coordenadas', font=fontDestaque)
		self.lblInfCoords.pack();

		self.coordsFrame = Frame(self.userInputFrame, pady=10)
		
		self.lblLat = Label(self.coordsFrame, text='Latitude', 
			font=('Verdana', 10, 'normal'))

		self.txtInputLatitude = Entry(self.coordsFrame, width=15, 
			font=fontNormal)
		self.txtInputLatitude.padx=5

		self.lblLong = Label(self.coordsFrame, text='Longitude', 
			font=('Verdana', 10, 'normal'))
		
		self.txtInputLongitude = Entry(self.coordsFrame, width=15, 
			font=fontNormal)


		self.lblLat.pack(side=LEFT)
		self.txtInputLatitude.pack(side=LEFT)
		self.lblLong.pack(side=LEFT)
		self.txtInputLongitude.pack(side=LEFT)
		self.coordsFrame.pack();


		self.btSearch = Button(self.userInputFrame, text='Buscar')
		self.btSearch['command'] = self.search
		self.btSearch.focus_force()
		self.btSearch.pack(side=LEFT)

		self.btSearchAll = Button(self.userInputFrame, text="Buscar todos")
		self.btSearchAll['command'] = self.searchAll
		self.btSearchAll.pack(side=LEFT);

		self.btSync = Button(self.userInputFrame, text="Atualizar DB")
		self.btSync['command'] = self.syncData
		self.btSync.pack(side=LEFT);

		self.userInputFrame.pack();

		self.resultFrame = Frame(self.root)

		self.lblResult = Label(self.resultFrame, text='Unidades de saúde mais próximas', font=fontNormal)
		self.lblResult.pack()
		
		self.txtOutputResult = Text(self.resultFrame, font=fontNormal, bg='white')
		self.txtOutputResult.width, self.txtOutputResult.height = 100, 100
		self.txtOutputResult.state = DISABLED

		self.txtOutputResult.pack()
		
		self.resultFrame.pack()

	def on_closing(self):
		self.userOpt = 4
		self.root.destroy()

	def syncData(self):
		print("sync")
		self.userOpt = 1

	def search(self):
		print("Search")
		self.userOpt = 2
		
	def searchAll(self):
		print("SearchAll")
		self.userOpt = 3

	def userOption(self):
		return self.userOpt

	def getLongitude(self):
		try:
			return float(self.txtInputLongitude.get())
		except:
			return 0.0

	def getLatitude(self):
		try:
			return float(self.txtInputLatitude.get())
		except:
			return 0.0

	def show(self, unSaude):
		if unSaude:
			self.txtOutputResult.text = unSaude.name

	def showAll(self, listaDeUnidades):
		if listaDeUnidades:
			str = ''
			for un in listaDeUnidades:
				str += un.name + '\n'
			self.txtOutputResult.text = str

	def menu(self):
		self.userOpt = 0
		self.root.update()
		pass
