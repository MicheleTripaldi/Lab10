from database.DAO import DAO
from model.model import Model

listObject = DAO.getAllCountry()
model = Model()
model.buildGraph(2016)
edges = DAO.getAllEdges(model.getIdMap())
print(len(listObject), len(edges))