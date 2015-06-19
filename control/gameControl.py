from model.labirinto import *

class GameControl:
	def __init__(self, filename):
                '''
                filename: diretorio do labirintio
                '''

		self.labirinto = labirintoFileFactory(filename)
		self.ratoVivo = True
		self.acabouJogo = False

	def visualizarGatoERato(self):
		#visualizar o gato e o rato
		for y in range(len(self.labirinto.labirinto)):
			a = ""
			for x in range(len(self.labirinto.labirinto[y])):
				if (x, y) == self.labirinto.gato:
					a+="G"
				elif (x,y) == self.labirinto.rato:
					a+="R"
				else:
					a+=self.labirinto.labirinto[y][x]
			print(a)

	def rodaTurno(self):
		#calcular a rota e achar a menor
		rota, peso = self.labirinto.acharMenorRota(self.labirinto.rato)


		#utiliza rota[1] pois rota[0] e a posicao atual do rato
		try:
			self.labirinto.moverRato(rota[-2]) #rota[-2] pega o penultimo termo da pilha de rota
			self.labirinto.gato = self.labirinto.gerarGato()
		except:
			self.ratoVivo = False
			self.acabouJogo = True 
			print('perdeu! :/')

		if self.labirinto.rato == self.labirinto.fim:
			print('ganhou! :D')
			print(self.labirinto.rato)
			self.acabouJogo = True

	def getGatoPos(self):
		return self.labirinto.gato
	def getRatoPos(self):
		return self.labirinto.rato
	def getLabirinto(self):
		return self.labirinto.labirinto
	def getTabelaCustos(self):
		return self.labirinto.tabelaCustos
	def getFacade(self):
		return (self.getGatoPos(),self.getRatoPos(),self.getLabirinto(),self.getTabelaCustos())
