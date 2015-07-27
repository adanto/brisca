#!/usr/bin/env python 


# Jugadores -> Numero de jugadores
# Turn -> 
# 		1: Otro
# 		2: Jugador Inteligente
def startGame(jugadores = 2):
	rondas = (40 - (jugadores * 3)) / jugadores

	cartas = [str(i) + "O" for i in [1,2,3,4,5,6,7, "S", "C", "R"]] + [str(i) + "C" for i in [1,2,3,4,5,6,7, "S", "C", "R"]] + [str(i) + "B" for i in [1,2,3,4,5,6,7, "S", "C", "R"]] + [str(i) + "E" for i in [1,2,3,4,5,6,7, "S", "C", "R"]]

	mano = []
	print "Primera carta:"
	mano.append(raw_input().upper())
	print "Segunda carta:"
	mano.append(raw_input().upper())
	print "Tercera carta:"
	mano.append(raw_input().upper())
	print "Pinte:"
	pinte = (raw_input().upper())

	print "Empieza -> 2, jugador, 1 CPU:"
	turn = int((raw_input().upper()))

	cartas = sorted(list(set(cartas) - set(mano)))
	cartas = sorted(list(set(cartas) - set(pinte)))
	
	print "Su mano:", mano
	print "Pinte:", pinte

	for _ in xrange(rondas):
		printCards(cartas)
		a = primeraAproximacion(pinte, turn, mano)
		if turn == 1:
			print "Tiramos", a[0],", el contrincante", a[1]
		else:
			print "El contrincante tira", a[1],", nosotros respondemos con", a[0]
		
		cartas.remove(a[1])
		mano.remove(a[0])
		print "Carta robada:"
		mano.append(raw_input().upper())
		cartas.remove(mano[2])
		turn = a[2] 
		print "Su mano:", mano
		print "Pinte:", pinte




def getValue(pinte, card1, card2):
	values = {
		"1": 11,
		"2": 0,
		"3": 10,
		"4": 0,
		"5": 0,
		"6": 0,
		"7": 0,
		"8": 0,
		"S": 2,
		"C": 3,
		"R": 4
	}

	val1 = values[card1[0]]
	val2 = values[card2[0]]
	if card1[1] == pinte[1]:
		if card2[1] == pinte[1]:
			return val1 + val2 if val2 > val1 else -(val1 + val2)
		else:
			return -(val1 + val2)
	else:
		if card2[1] == pinte[1]:
			return val1 + val2
		else:
			if card1[1] == card2[1]:
				return val1 + val2 if val2 > val1 else -(val1 + val2)
			else:
				return -(val1 + val2)

def valueCards(pinte, card):
	values = {
		"1": 11,
		"2": 0,
		"3": 10,
		"4": 0,
		"5": 0,
		"6": 0,
		"7": 0,
		"8": 0,
		"S": 2,
		"C": 3,
		"R": 4
	}
	val = 0
	if pinte[1] == card[1]:
		return 20 + values[card[0]]
	else:
		return values[card[0]]

def whoWins(p, c1, c2):
	if c1[1] == p[1]:
		if c2[1] == p[1]:
			return 1 if valueCards(p, c1) > valueCards(p, c2) else 2
		else:
			return 1
	else:
		if c2[1] == p[1]:
			return 2
		else:
			if c1[1] == c2[1]:
				return 1 if valueCards(p, c1) > valueCards(p, c2) else 2
			else:
				return 1

def printCards(cartas):
	c = [str(i) + "C" for i in [1,2,3,4,5,6,7, "S", "C", "R"]] 
	e = [str(i) + "E" for i in [1,2,3,4,5,6,7, "S", "C", "R"]] 
	b = [str(i) + "B" for i in [1,2,3,4,5,6,7, "S", "C", "R"]] 
	o = [str(i) + "O" for i in [1,2,3,4,5,6,7, "S", "C", "R"]] 

	copas = []
	for i in c:
		copas.append(i if i in cartas else "  ")
	espadas = []
	for i in e:
		espadas.append(i if i in cartas else "  ")
	bastos = []
	for i in b:
		bastos.append(i if i in cartas else "  ")
	oros = []
	for i in o:
		oros.append(i if i in cartas else "  ")

	print ", ".join(copas)
	print ", ".join(espadas)
	print ", ".join(bastos)
	print ", ".join(oros)


def primeraAproximacion(pinte, turn, mano):
	print "\n#############################"
	if turn == 2:
		print "Movimiento del contrincante:"
		cartaMesa = raw_input().upper()
		values = []
		for i in mano:
			values.append(getValue(pinte, cartaMesa, i))
		return mano[values.index(max(values))], cartaMesa, 2 if whoWins(pinte, cartaMesa, mano[values.index(max(values))]) else 1
	elif turn == 1:
		values = []
		for i in mano:
			values.append(valueCards(pinte, i))
		carta = mano[values.index(min(values))] 
		print "Tiramos", mano[values.index(min(values))] 
		print "Movimiento del contrincante"
		cartaMesa = raw_input().upper()
		return carta, cartaMesa, 1 if whoWins(pinte, carta, cartaMesa) == 1 else 2
	else:
		pass











if __name__ == "__main__":
	startGame()