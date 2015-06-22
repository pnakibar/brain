from model.labirinto import *

class GameControl:
	def __init__(self, filename):
                '''
                filename: diretorio do labirintio
                '''

		self.labirinto = labirintoFileFactory(filename)
		self.ratoVivo = True
		self.acabouJogo = False


	def rodaTurno(self):
            if not self.acabouJogo:
		#calcular a rota e achar a menor
		rota, peso = self.labirinto.acharMenorRota(self.labirinto.rato)

		#utiliza rota[1] pois rota[0] e a posicao atual do rato
                self.labirinto.gato = self.labirinto.gerarGato()
                self.labirinto.moverRato(rota[-2]) #rota[-2] pega o penultimo termo da pilha de rota
                
                if self.labirinto.gato == self.labirinto.rato:
			self.ratoVivo = False
			self.acabouJogo = True 

		if self.labirinto.rato == self.labirinto.fim:
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
