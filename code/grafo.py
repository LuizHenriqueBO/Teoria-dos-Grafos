from aresta import *
from vertice import *


class Grafo(object):
    def __init__(self):
        self.lista_aresta = list()
        self.lista_vertice = list()

    def add_vertice(self, nome_vertice, valor=0):
        vert = Vertice(nome_vertice, valor)
        self.lista_vertice.append(vert)
        return vert

    # verificar se pode mais de uma aresta no mesmo origem e destino
    def add_aresta(self, nome_aresta, origem, destino, valor_aresta=0):
        
        if(self.get_aresta(nome_aresta) == None):
            
            if(self.verifica_origem_e_destino_da_aresta(origem, destino) == False):
                v_origem = self.get_vertice(origem)
                v_destino = self.get_vertice(destino)

                if(v_origem is None):
                    v_origem = self.add_vertice(origem)
                
                if(v_destino is None):
                    v_destino = self.add_vertice(destino)
        
                arest = Aresta(nome_aresta, valor_aresta, v_origem, v_destino)
                self.lista_aresta.append(arest)

                return True
            return False
        return False


    def get_aresta(self, nome_aresta):
        for arest in self.lista_aresta:
            if arest.get_aresta_nome() == nome_aresta:
                return arest
        return None


    def get_vertice(self, nome_vertice):
        for vert in self.lista_vertice:
            if vert.get_vertice_nome() == nome_vertice:
                return vert
        return None


    def get_aresta_vertice_origem(self, nome_vertice, lista_aresta=[]):
        if lista_aresta == []:
            lista_aresta = self.lista_aresta
        l_arest = []
        for i in lista_aresta:
            if i.get_aresta_origem().get_vertice_nome() == nome_vertice:
                l_arest.append(i)
        return l_arest

    def get_aresta_vertice_destino(self, nome_vertice, lista_aresta=[]):
        if lista_aresta == []:
            lista_aresta = self.lista_aresta
        l_arest = []
        for i in lista_aresta:
            if i.get_aresta_destino().get_vertice_nome() == nome_vertice:
                l_arest.append(i)
        return l_arest


    def get_aresta_vertice_all(self, nome_vertice):
        lista_arest = []
        lista_arest.append(self.get_aresta_vertice_destino(nome_vertice))
        lista_arest.append(self.get_aresta_vertice_origem(nome_vertice))
        return lista_arest


    def __str__(self):
        resultado = []
        for vert in self.lista_vertice:
            resultado.append(vert.get_vertice_nome())
            resultado.append(" : ")
            arestas = []
            for arest in self.get_aresta_vertice_origem(vert.get_vertice_nome()):
                arestas.append("(")
                arestas.append("".join(arest.get_aresta_nome()))
                arestas.append(")")
                arestas.append(arest.get_aresta_destino().get_vertice_nome())
                arestas.append(",")
            resultado.append(" ".join(arestas))
            resultado.append("\n\n")
        return ''.join(resultado)



    # verifico se a origem e destino já existem no grafo
    def verifica_origem_e_destino_da_aresta(self, origem, destino):
        for arest in self.lista_aresta:
            if arest.get_aresta_origem().get_vertice_nome() == origem and arest.get_aresta_destino().get_vertice_nome() == destino :
                return True
        return False
    

    # retorna a ordem do grafo -> "quantidade de bolinhas"
    def get_ordem(self):
        return len(self.lista_vertice)

    # # retorna o grau de um vertice
    def get_grau(self, vertice):
        return len(self.get_aresta_vertice_origem(vertice))

    def get_vertices(self):
        return [vert.get_vertice_nome() for vert in self.lista_vertice]

    
    def is_completo(self):
        ordem = self.get_ordem()

        for vert in self.lista_vertice:
            if(not(self.get_grau(vert.get_vertice_nome()) == ordem-1)):
                return False
        return True


    def verificacao_recursiva_conexo(self, lista_vert, lista_arest, vertice_origem, aresta_origem, lista_visitados):
        if(vertice_origem == None): # verifica se o vertice de origem existe
            return
        lis_aresta_origem = self.get_aresta_vertice_destino(vertice_origem.get_vertice_nome(), lista_arest) # pegando todas as aresta do vertice de origem
        lis_aresta_destino = self.get_aresta_vertice_origem(vertice_origem.get_vertice_nome(), lista_arest) # pegando todas as aresta do vertice de origem      
        if( lis_aresta_destino == [] ) and ( lista_vert == [] ): # verifico se ja acabou a lista de aresta e de vertices, então retorna os vertices encontrados
           return
        if aresta_origem in lista_arest:
            lista_arest.remove(aresta_origem)

        if vertice_origem not in lista_visitados:
            lista_visitados.append(vertice_origem)

        if (len(lis_aresta_destino) == 1):
            lista_vert.remove(vertice_origem)

        for arest in lis_aresta_destino:
            if(arest.get_aresta_destino() in lista_vert):
                self.verificacao_recursiva_conexo(lista_vert, lista_arest, arest.get_aresta_destino(), arest, lista_visitados) # chama a recursão
        return lista_visitados



    def is_conexo(self):
        for vert in self.lista_vertice:
            lista_visitados = []
            lista_vert = self.lista_vertice[:]
            lista_arest = self.lista_aresta[:]
            self.verificacao_recursiva_conexo(lista_vert, lista_arest, vert, None, lista_visitados )
            
            for i in lista_visitados:
                #print(i.get_vertice_nome())
                if i in lista_vert:
                    lista_vert.remove(i)
            #print("\n")
             
            if lista_vert == []:
                return True
        return False



    def get_adjacentes(self, nome_vertice):
        l_aresta = self.get_aresta_vertice_origem(nome_vertice)
        lista_vert = []
        for aresta in l_aresta:
            lista_vert.append(aresta.get_aresta_destino().get_vertice_nome())
        return lista_vert



    # def verificacao_recursiva_arvore(self, lista_vert, vertice_origem, lista_visitados):

    #     if(vertice_origem == None): # verifica se o vertice de origem existe            
    #         return 
    #     lis_aresta = self.get_aresta_vertice_origem(vertice_origem.get_vertice_nome()) # pegando todas as aresta do vertice de origem
    #     if( lis_aresta == None ) and ( lista_vert == None ): # verifico se ja acabou a lista de aresta e de vertices, então retorna os vertices encontrados
    #         return
    #     if( lis_aresta == None ) and ( lista_vert != None ): # se minha lista de aresta for vazia e ainda tenho vertice, então é falso
    #         return
    #     if vertice_origem in lista_vert:
    #         lista_visitados.append(vertice_origem)
    #         print("removendo o vertice: ",vertice_origem.get_vertice_nome())
    #         lista_vert.remove(vertice_origem)
    #     for arest in lis_aresta:
    #         #print(arest.get_aresta_nome())
    #         if(arest.get_aresta_destino()):
    #             self.verificacao_recursiva_arvore(lista_vert, arest.get_aresta_destino(), lista_visitados) # chama a recursão
    #     return lista_visitados



    # def is_arvore(self):
    #     if(self.is_conexo() == True){

    #     }
        



g = Grafo()
# g.add_aresta('a1','A','B',10)
# g.add_aresta('a2','A','C',5)
# g.add_vertice('Y')
# g.add_aresta('a4','B','D',20)
# g.add_aresta('a5','B','A',15)


g.add_aresta('a1','A','B',10)
# g.add_aresta('a2','A','C',10)
# g.add_aresta('a3','A','D',10)

# g.add_aresta('a4','B','A',10)
g.add_aresta('a2','B','C',10)
g.add_aresta('a3','B','D',10)
g.add_aresta('a4','E','C',10)


g.add_aresta('a5','C','A',10)
g.add_aresta('a6','C','B',10)
# g.add_aresta('a9','C','D',10)

g.add_aresta('a10','D','A',10)
g.add_aresta('a11','D','B',10)
g.add_aresta('a12','D','C',10)



#print(g.is_completo())

print(g.is_conexo())
#print(g.get_vertices()) 

#print(g.get_ordem()) # imprime a ordem
#print(g.get_grau('A')) # imprime o grau dos vertices
#print(g.get_adjacentes('B'))
#g.add_aresta('a1','D','C',11) # (adicionar aresta de mesmo nome)ISSO NÃO PODE ACONTECER !, ok funcionando! 

#g.add_aresta('a50','A','B',30) # (adicionar mais de uma aresta pra o mesmo origem e destino )ISSO NÃO PODE ACONTECER !, ok funcionando!

print(str(g))
