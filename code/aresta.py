
class Aresta(object):
    
    def __init__(self, nome, valor, origem, destino):
        self.nome = nome
        self.valor = valor
        self.origem = origem
        self.destino = destino



    def set_aresta_nome(self,nome):
        self.nome = nome

    def set_aresta_valor(self, valor):
        self.valor = valor

    def set_aresta_origem(self, origem):
        self.origem = origem

    def set_aresta_destino(self, destino):
        self.destino = destino




    def get_aresta_nome(self):
        return self.nome

    def get_aresta_valor(self):
        return self.valor

    def get_aresta_origem(self):
        return self.origem

    def get_aresta_destino(self):
        return self.destino


# Aresta("a1", 10, "A", "B")

# arestas = []

# Grafo.addAresta("e1","A", "B", 10)
#     if not Grafo.hasVertice("A"):
#         Grafo.addVertice("A")
#     if not Gra...

#     Grafo.arestas = Aresta("e1", 10, Grafo.getVertice("A"), Grafo.getVertice("B"))