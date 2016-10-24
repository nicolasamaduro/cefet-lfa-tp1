import re
from AFN import AFN

class leitorTexto(object):
    """ Le a gramatica em um arquivo passado como argumento
        na linha de comando                                 """

    def __init__(self, str):
        self.str = str

    def getAFN(self):
        with open(self.str, 'r') as file:
            gr = file.read()

            afn = AFN()

            abreChaves = fechaChaves = countChaves = 0


            # Percorre a gramatica retirando informacoes            
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

                                afn.estados.append(gr[i])

                        # Pega os elementos do alfabeto e coloca em uma lista
                        elif countChaves == 2:
                            if gr[i].isdigit():
                                afn.alfabeto.append(gr[i])

                # Pega os estadosIniciais e Trata as transicoes prenchendo uma matriz afn
                else:
                    # Pega os estadosIniciais
                    for i in range(fechaChaves,len(gr)):
                        if gr[i].isalpha():
                            afn.estadosIniciais.append(gr[i])

                    # Trata as transicoes prenchendo uma matriz afn
                    # Cria matriz afn com o caracter '-'
                    afn.transicoes = [['-' for i in range(len(afn.alfabeto))] for j in range(len(afn.estados))]
                    # Substring de gr apenas com as transicoes
                    auxGr = gr[abreChaves + 1:fechaChaves]
                    # Retira os espacos
                    auxGr = re.sub(r' ', '', auxGr)
                    # Lista com todas as transicoes
                    listaTransicoes = auxGr.split(',')
                    # Percorre todas as transicoes e coloca na matriz
                    for i in range(len(listaTransicoes)):
                        t = listaTransicoes[i].split('->')
                        # Verifica se e' estado final - possui lambda
                        if t[1] == '\xce\xbb':
                            afn.estadosFinais.append(t[0])
                        else:
                            indexEstadoIda = afn.estados.index(t[0])
                            # Checa se a transicao vai pra um estado existente

                            indexAlfabeto = afn.alfabeto.index(t[1][0])
                            if len(t[1]) == 1:
                                if t[1] not in afn.estados:
                                    afn.estadosFinais.append(t[1][0])
                                    afn.estados.append(t[1][0])
                                    afn.transicoes.append(['-','-'])
                                # Checa se a transicao ja esta indo para outro estado
                                if afn.transicoes[indexEstadoIda][indexAlfabeto] != '-':
                                    afn.transicoes[indexEstadoIda][indexAlfabeto] += ',' + t[1][0]
                                else:
                                    afn.transicoes[indexEstadoIda][indexAlfabeto] = t[1][0]
                            else:
                                # Checa se a transicao ja esta indo para outro estado
                                if afn.transicoes[indexEstadoIda][indexAlfabeto] != '-':
                                    afn.transicoes[indexEstadoIda][indexAlfabeto] += ','+t[1][1]
                                else:
                                    afn.transicoes[indexEstadoIda][indexAlfabeto] = t[1][1]


                abreChaves += 1
                fechaChaves += 1
                countChaves += 2

        return afn