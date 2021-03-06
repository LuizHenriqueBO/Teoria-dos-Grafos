from sys import maxsize

class Vertice(object):

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        self.cor = 'branco'
        self.distancia = maxsize
        self.predecessor = None
        self.grau_entrada = 0
        self.grau_saida = 0
        self.tempo_entrada = None
        self.tempo_saida = None


    def set_vertice_cor(self, cor):
        self.cor = cor

    def set_vertice_valor(self, valor):
        self.valor = valor

    def set_vertice_distancia(self, distancia):
        self.distancia = distancia

    def set_vertice_predecessor(self, predecessor):
        self.predecessor = predecessor

    def set_vertice_grau_entrada(self, grau_entrada):
        self.grau_entrada = grau_entrada
    
    def set_vertice_grau_saida(self, grau_saida):
        self.grau_saida = grau_saida

    def set_vertice_tempo_entrada(self, tempo_entrada):
        self.tempo_entrada = tempo_entrada
    
    def set_vertice_tempo_saida(self, tempo_saida):
        self.tempo_saida = tempo_saida




    def add_vertice_grau_entrada():
        set_vertice_grau_entrada(get_grau_entrada+1)

    def add_vertice_grau_saida():
        set_vertice_grau_saida(get_grau_saida+1)



    def get_vertice_nome(self):
        return self.nome
        
    def get_vertice_cor(self):
        return self.cor

    def get_vertice_valor(self):
        return self.valor

    def get_vertice_distancia(self):
        return self.distancia

    def get_vertice_predecessor(self):
        return self.predecessor

    def get_vertice_grau_entrada(self):
        return self.grau_entrada
    
    def get_vertice_grau_saida(self):
        return self.grau_saida

    def get_vertice_tempo_entrada(self):
        return self.tempo_entrada
    
    def get_vertice_tempo_saida(self):
        return self.tempo_saida





