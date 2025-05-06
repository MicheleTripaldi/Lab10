import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._country = DAO.getAllCountry()
        self._grafo = nx.Graph()
        self._idMapCountry = {}
        for con in self._country:
            self._idMapCountry[con.CCode] = con


    def buildGraph(self, year):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._country)
        self.addAllEdges(year)
    def addAllEdges(self,year):
       # self._grafo.clear()

        allEdges = DAO.getAllEdges()
        for edge in allEdges:
            u = self._idMapCountry[edge.state1no]
            v = self._idMapCountry[edge.state2no]
            if edge.year <= year and edge.conttype == 1:
                print(edge)
                self._grafo.add_edge(u, v)


    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

    def getIdMap(self):
        return self._idMapCountry