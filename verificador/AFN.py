from AutomatoFormal import AutomatoFormal
from AFD import AFD

class AFN(AutomatoFormal):
    def __init__(self):
        super(AFN,self).__init__()

    def verificaPalavra(self, palavra):
        pass

    def defineEstadosFinaisAFD(self):
        """ Percorre estadosAFD verificando onde esta um estado final da AFN
            gerando a lista estadosFinaisAFD                                 """

        for e in self.estadosFinais:
            for e_AFD in self.afd.estados:
                if e in e_AFD and e_AFD not in self.afd.estadosFinais:
                    self.afd.estadosFinais.append(e_AFD)

    def toAFD(self):
        """ Passa um AFN pra AFD"""
        self.afd = AFD()

        self.afd.alfabeto=self.alfabeto
        cont = 0

        # Coloca na estadosAFD os estados iniciais
        self.afd.estados = [','.join(self.estadosIniciais)]  # Passa do formato ['A','B'] -> ['A,B']

        # Cria o AFD
        while cont != len(self.afd.estados):

            # Inicia o afd
            if cont == 0:
                self.afd.transicoes = [['-' for i in range(len(self.alfabeto))]]
            else:
                self.afd.transicoes.append(['-' for i in range(len(self.alfabeto))])

            # Percorre cada estado em estadosAFD e preenche o afd
            # com as respectivas transicoes
            for e in self.afd.estados[cont]:
                if e != ',':
                    indexEstado = self.estados.index(e)
                    for a in self.alfabeto:
                        indexAlfabeto = self.alfabeto.index(a)
                        transicao = self.transicoes[indexEstado][indexAlfabeto]
                        if transicao != '-':
                            if self.afd.transicoes[-1][indexAlfabeto] != '-':
                                self.afd.transicoes[-1][indexAlfabeto] += ',' + transicao
                            else:
                                self.afd.transicoes[-1][indexAlfabeto] = transicao
            self.afd.estados = self.afd.atualizaEstados(self.afd.transicoes[-1])
            cont += 1

        # Determina o estadoInicial
        self.afd.estadosIniciais = [self.afd.estados[0]]

        # Determina os estadosFinaisAFD
        self.defineEstadosFinaisAFD()


