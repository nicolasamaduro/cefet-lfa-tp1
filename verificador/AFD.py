from AutomatoFormal import AutomatoFormal

class AFD(AutomatoFormal):
    def __init__(self):
        super(AFD, self).__init__()

    def verificaPalavra(self, palavra):
        estadoAtual=self.estadosIniciais
        indexEstado=0
        indexAlfabeto=0
        for digito in palavra:
            if not (digito in self.alfabeto):
                return False
            else:
                for e in self.estados:
                    if (e==estadoAtual):
                        indexEstado = self.estados.index(e)
                for d in self.alfabeto:
                    if (d==digito):
                        indexAlfabeto = self.alfabeto.index(d)
                estadoAtual=self.transicoes[indexEstado][indexAlfabeto]
                if estadoAtual == '-':
                    return False
        if estadoAtual in self.estadosFinais:
            return True
        else:
            return False



