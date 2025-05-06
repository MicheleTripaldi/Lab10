import flet as ft


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
            self._view._txt_result.controls.append(ft.Text(f" Confine{n}-{arco}"))
            n += 1

        self._view.update_page()

