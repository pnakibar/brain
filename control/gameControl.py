from model.labirinto import *

class GameControl:
	def __init__(self, filename):
                '''
                filename: diretorio do labirintio
                '''

		self.labirinto = labirintoFileFactory(filename)
		self.ratoVivo = True
		self.acabouJogo = False
		self.rota = []
		self.rotaAtual = []

                if (self.checkPerdeuJogo()):
                    self.perdeuJogo()

        

        def perdeuJogo(self):
            self.ratoVivo = False
            self.acabouJogo = True 

        def ganhouJogo(self):
            self.acabouJogo = True

	def rodaTurno(self):
            if not self.acabouJogo:
		#calcular a rota e achar a menor
                try:
			rota, peso = self.labirinto.acharMenorRota(self.labirinto.rato)
			self.rotaAtual = rota[:-2]

                except Exception:
                    self.perdeuJogo()
                    raise

	    	print(rota)
                    
		#utiliza rota[1] pois rota[0] e a posicao atual do rato
                self.labirinto.gato = self.labirinto.gerarGato()
                self.labirinto.moverRato(rota[-2]) #rota[-2] pega o penultimo termo da pilha de rota
		self.rota.append(rota[-2])
                
                if self.labirinto.gato == self.labirinto.rato:
		    self.perdeuJogo()

		if self.labirinto.rato == self.labirinto.fim:
                    self.ganhouJogo()

        def checkPerdeuJogo(self):
            return (self.getGatoPos()==self.getRatoPos())
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
