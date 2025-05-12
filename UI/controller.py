import flet as ft
from database.DAO import DAO
from model.model import Model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        anno = self._view._txtAnno.value
        if anno is None or anno == "" or not anno.isdigit():
            self._view.create_alert(" Inserire l'anno")
            return
        if int(anno) < 1861 or int(anno) > 2016:
            self._view.create_alert(" Inserire un anno valido tra il 1861 e il 2016")
            return
        lista_archi= []
        anno = int(anno)
        self._model.buildGraph(anno)
        lista_archi = self._model._grafo.edges()

        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo creato correttamente"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodi()}nodi"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumArchi()}archi"))

        n = 1
        for arco in lista_archi:

            self._view._txt_result.controls.append(ft.Text(f" Stato{n}-{arco}"))
            #self._view._txt_result.controls.append(ft.Text(f" Grado Nodo:{len(self._model.gradoNodo(arco))}"))
            n += 1

        lista_nodi = []
        lista_nodi = DAO.getCountry(anno)
        n = 1
        for nodo in lista_nodi:
            if self._model.gradoNodo(nodo) != 0:
                self._view._txt_result.controls.append(ft.Text(f" Stato{n}-{nodo}: Ha grado{self._model.gradoNodo(nodo)}"))
                n += 1

        self._view._txt_result.controls.append(ft.Text(f"Il numero di componenti connesse del garfo é:{self._model.getPartiConnesse()}"))

        self._view.update_page()

    def handleRaggiungibili(self, e):
        stato = self._view._ddStati.value
        anno = self._view._txtAnno.value
        if stato is None or stato == "":
            self._view.create_alert(" Inserire lo stato valido")
            return
        if anno is None or anno == "" or not anno.isdigit():
            self._view.create_alert(" Inserire l'anno")
            return
        if int(anno) < 1861 or int(anno) > 2016:
            self._view.create_alert(" Inserire un anno valido tra il 1861 e il 2016")
            return
        self._model.buildGraph(anno)
        self._view._txt_result.controls.clear()
        listaRagg = self._model.getComponenteConnessa(stato)
        self._view._txt_result.controls.append(ft.Text(f"Ho calcolato la componente connessa:"))
        for c in listaRagg:
            self._view._txt_result.controls.append(ft.Text(f"{c.StateNme} è un vicino"))
        self._view.update_page()




    def fillddStati(self):
        lista_stati = self._model.stati()
        for stato in lista_stati:
            self._view._ddStati.options.append(ft.dropdown.Option(text=stato.StateNme, key=stato.CCode))


