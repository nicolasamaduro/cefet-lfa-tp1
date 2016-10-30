class AF(object):

    def __init__(self):
        self.alfabeto=[]
        self.estados=[]
        self.estadosFinais=[]
        self.estadosIniciais=[]
        self.transicoes=[]


    def verificaPalavra(self,palavra):
        raise NotImplementedError

    def atualizaEstados(self,novosEstados):
        """ Dada lista de estados (novosEstados) checa se eles ja estao
            na lista estados
            Sim: retorna estados
            Nao: faz append do novo estado no final de estados       """
        for e in novosEstados:
            if e != '-':
                # Checa se, por exemplo, 'A,B' ou 'B,A' esta em estadosAFD
                if e in self.estados or e[::-1] in self.estados:
                    pass
                else:
                    self.estados.append(e)
        return self.estados
