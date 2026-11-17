

from model.model import Model

class Controller:
    def __init__(self, view, model: Model):
        self._view = view
        self._model = model

    def handle_statistiche(self, e):
        serate = int(self._view.dd_serate.value)
        if serate is None:
            self._view.mostra('Inserisci prima un numero di serate')
        else:
            statistiche_formattate = []
            statistiche_per_genere = self._model.get_statistiche_per_genere(serate)
            for el in statistiche_per_genere:
                statistiche_formattate.append(f"{el[0]}: Numero Proiezioni {el[1]}, Media Voti {el[2]:.2f}")
            self._view.mostra(statistiche_formattate)


    def handle_programma(self, e):
        self._model.trova_programma_ottimo(int(self._view.dd_serate.value))
        if self._model.miglior_programma is not None:
            self._view.mostra(self._model.miglior_programma)
        else:
            self._view.mostra(['Errore non è stato trovato nessun programma'])
