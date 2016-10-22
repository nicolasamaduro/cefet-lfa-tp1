
def atualizaEstadosAFD(estadosAFD, novosEstados):
	""" Dada lista de estados (novosEstados) checa se eles ja estao
		na lista estadosAFD
		Sim: retorna estadosAFD
		Nao: faz append do novo estado no final de estadosAFD       """
	
	for e in novosEstados:
		if e != '-':
			# Checa se, por exemplo, 'A,B' ou 'B,A' esta em estadosAFD
			if e in estadosAFD or e[::-1] in estadosAFD:
				pass
			else:
				estadosAFD.append(e)

	return estadosAFD
		

def DefineEstadosFinaisAFD(estadosAFD, estadosFinaisAFN):
	""" Percorre estadosAFD verificando onde esta um estado final da AFN 
	    gerando a lista estadosFinaisAFD                                 """

	estadosFinaisAFD = []

	for e in estadosFinaisAFN:
		if e != ',':
			for e_AFD in estadosAFD:
				if e in e_AFD:
					estadosFinaisAFD.append(e_AFD)

	return estadosFinaisAFD


def afn_to_afd(estadosAFN, alfabeto, estadosIniciaisAFN, estadosFinaisAFN, afn):
	""" Passa um AFN pra AFD"""

	cont = 0
	afd = []

	# Coloca na estadosAFD os estados iniciais
	estadosAFD = [','.join(estadosIniciaisAFN)] # Passa do formato ['A','B'] -> ['A,B']

	# Cria o AFD
	while cont != len(estadosAFD):

		# Inicia o afd
		if cont == 0:
			afd = [['-' for i in range(len(alfabeto))]]
		else:
			afd.append(['-' for i in range(len(alfabeto))])

		# Percorre cada estado em estadosAFD e preenche o afd
		# com as respectivas transicoes
		for e in estadosAFD[cont]:
			if e != ',' and e != 'Z':
				indexEstado = estadosAFN.index(e)
				for a in alfabeto:
					indexAlfabeto = alfabeto.index(a)
					transicao = afn[indexEstado][indexAlfabeto]
					if transicao != '-':
						if afd[-1][indexAlfabeto] != '-':
							afd[-1][indexAlfabeto] += ','+transicao
						else:
							afd[-1][indexAlfabeto] = transicao

		
		estadosAFD = atualizaEstadosAFD(estadosAFD, afd[-1])
		cont += 1

	# Determina o estadoInicial
	estadoInicialAFD = [estadosAFD[0]]

	# Determina os estadosFinaisAFD
	estadosFinaisAFD = DefineEstadosFinaisAFD(estadosAFD,','.join(estadosFinaisAFN))

	return estadosAFD, estadoInicialAFD, estadosFinaisAFD, afd