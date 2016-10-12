import re

class leitorTexto(object):

    def __init__(self, str):
        self.str = str

    def getGR(self):
        with open(self.str, 'r') as file:
            gr = file.read()

            abreChaves = fechaChaves = countChaves = 0
            estados = []
            alfabeto = []
            while (countChaves < 6):

                # Pega os indices do { e }
                abreChaves = gr.find('{', abreChaves, len(gr))
                fechaChaves = gr.find('}', fechaChaves, len(gr))

                # Trata  os estados e o alfabeto colocando ambos
                # em uma lista separada
                if countChaves <= 2:
                    for i in range(abreChaves + 1, fechaChaves):
                        # Pega os estados e coloca em uma lista
                        if countChaves == 0:
                            if gr[i].isalpha():
                                estados.append(gr[i])

                        # Pega os elementos do alfabeto e coloca em uma lista
                        elif countChaves == 2:
                            if gr[i].isdigit():
                                alfabeto.append(gr[i])

                # Trata as transicoes prrenchendo uma matriz afn
                else:
                    # Cria matriz afn com valor -1
                    afn = [[-1 for i in range(len(alfabeto))] for j in range(len(estados))]
                    # Substring de gr apenas com as transicoes
                    auxGr = gr[abreChaves + 1:fechaChaves]
                    # Retira os espacos
                    auxGr = re.sub(r' ', '', auxGr)
                    # Lista com todas as transicoes
                    listaTransicoes = auxGr.split(',')
                    # Percorre todas as transicoes e coloca na matriz
                    for i in range(len(listaTransicoes)):
                        t = listaTransicoes[i].split('->')
                        indexEstadoIda = estados.index(t[0])
                        # Checa se a transicao vai pra um estado existente
                        if len(t[1]) == 2:
                            indexAlfabeto = alfabeto.index(t[1][0])
                            afn[indexEstadoIda][indexAlfabeto] = t[1][1]
                        else:
                            indexAlfabeto = alfabeto.index(t[1])
                            afn[indexEstadoIda][indexAlfabeto] += ',Z'

                abreChaves += 1
                fechaChaves += 1
                countChaves += 2

        return afn