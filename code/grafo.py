from aresta import *
from vertice import *


class Grafo(object):
    def __init__(self):
        self.lista_aresta = list()
        self.lista_vertice = list()

    def add_vertice(self, nome, valor=0):
        vert = Vertice(nome, valor)
        self.lista_vertice.append(vert)
        return vert

    # verificar se pode mais de uma aresta no mesmo origem e destino
    def add_aresta(self, nome, origem, destino, valor=0):
        
        if(self.get_aresta(nome) == None):
        
            v_origem = self.get_vertice(origem)
            v_destino = self.get_vertice(destino)

            if(v_origem is None):
                v_origem = self.add_vertice(origem)
            
            if(v_destino is None):
                v_destino = self.add_vertice(destino)
    
            arest = Aresta(nome, valor, v_origem, v_destino)
            self.lista_aresta.append(arest)

            return True

        return False


    def get_aresta(self, nome):
        for arest in self.lista_aresta:
            if arest.get_nome() == nome:
                return arest
        return None




    def get_vertice(self, nome):
        for vert in self.lista_vertice:
            if vert.get_nome() == nome:
                return vert
        return None
    

    def get_aresta_vertice(self, nome):
        lista = []
        for i in self.lista_aresta:
            if i.origem.nome == nome:
                lista.append(i)
        return lista


    def __str__(self):
        resultado = []
        for vert in self.lista_vertice:
            resultado.append(vert.nome)
            resultado.append(" : ")
            arestas = []
            for arest in self.get_aresta_vertice(vert.nome):
                arestas.append("(")
                arestas.append("".join(arest.nome))
                arestas.append(")")
                arestas.append(arest.destino.nome)
                arestas.append(",")
            resultado.append(" ".join(arestas))
            resultado.append("\n\n")
        return ''.join(resultado)




g = Grafo()
g.add_aresta('a1','A','B',10)
g.add_aresta('a2','A','C',5)
g.add_aresta('a3','A','D',1)
g.add_aresta('a4','B','D',20)
g.add_aresta('a5','B','A',15)
g.add_aresta('a1','D','C',11)
print(str(g))
