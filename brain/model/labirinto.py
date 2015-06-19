from random import randint
from loadFile import *

class Labirinto:
	def __init__(self, lab, tabCustos):
		self.labirinto = lab
		self.tabelaCustos = tabCustos
		self.inicio = self.acharInicio()
		self.fim = self.acharFim()
		self.rato = self.inicio

		self.gato = self.gerarGato()

		self.moverCima = lambda x, y: (x, y - 1)
		self.moverBaixo = lambda x, y: (x, y + 1)
		self.moverDireita = lambda x, y: (x + 1, y)
		self.moverEsquerda = lambda x, y: (x - 1, y)
		self.movimentos = [self.moverCima, self.moverBaixo, self.moverDireita, self.moverEsquerda]



	def printMatrix(self, m):
		for e in m:
			print(e)

	def printLabirinto(self): printMatrix(self.labirinto)
	def printTabelaCustos(self): printMatrix(self.tabelaCustos)

	def acharChar(self, c):
		c = c.upper()
		for y in range(0, len(self.labirinto)):
			for x in range(0, len(self.labirinto[y])):
				if self.labirinto[y][x] == c:
					return x, y

	def acharInicio(self): return self.acharChar('S')
	def acharFim(self):	return self.acharChar('F')

	def moverRato(self, newPos):
		if newPos == self.gato:
			raise Exception("Gato no caminho!")
		else:
			self.rato = newPos

	def gerarGato(self):
		'''
		TODO:
			Verificar se o gato nao pode aparecer aonde o rato esta
		'''
		x = randint(0, len(self.labirinto[0])-1)
		y = randint(0, len(self.labirinto)-1)


		if (x,y) == self.rato or self.labirinto[y][x] == '0':
			return self.gerarGato()
		'''
		while self.labirinto[y][x] == '0' or ((x,y) == self.rato):
			x = randint(0, len(self.labirinto[0])-1)
			y = randint(0, len(self.labirinto)-1)
		'''
		return x,y

	def possiveisMovimentos(self, pos):
	    possiveis = []
	    posX, posY = pos

	    for mov in [self.moverCima, self.moverEsquerda]:
	        x, y = mov(posX, posY)

	        if self.labirinto[y][x] != '0':
	            possiveis.append((x, y))

	    return possiveis

	def fazRotas(self, pos):
	    # DONE: acha as rotas de tras para frente
	    rotas = []

	    def loop(pos, rota):
	        r = rota[:]  # copia da lista, Python trata as listas por referencia
	        r.append(pos)
	        if (pos == self.rato):
	            rotas.append(r)
	        else:
	            for p in self.possiveisMovimentos(pos):
	            	loop(p, r)

	    loop(self.fim, [])
	    return rotas

	def calcularCustoRota(self, rota):
		peso = 0
		for x, y in rota:
			if (x,y) == self.gato:
				peso = peso + float("inf")
			else:
				peso = peso + int(self.tabelaCustos[y][x])

		return peso

	def acharMenorRota(self, pos):
		rotasPossiveis = self.fazRotas(pos)

		menorRota = rotasPossiveis[0]
		menorPesoRota = self.calcularCustoRota(menorRota)

		for e in rotasPossiveis:
			pesoRota = self.calcularCustoRota(e)

			if menorPesoRota > pesoRota:
				menorPesoRota = pesoRota
				menorRota = e

		return menorRota, menorPesoRota

def labirintoFileFactory(filename):
	labirinto, tabelaCustos = carregarArquivo(filename)
	return Labirinto(labirinto, tabelaCustos)
