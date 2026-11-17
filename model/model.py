import copy

from database.dao import Dao
from model.film import Film


class Model:

    def __init__(self):
        self.miglior_programma = None
        self.migliore_media_programma = None
    def get_statistiche_per_genere(self,n):
        statistiche_per_genere = Dao.get_statistiche(n)
        return statistiche_per_genere
    def get_film(self,n):
        film = Dao.get_film(n)
        return film
    def trova_programma_ottimo(self,n):
        film = Dao.get_film(n)
        generi_usati = {}
        self.miglior_programma = None
        self.migliore_media_programma = None
        self.ricorsione(n, film, 1, [], 0, generi_usati, None)

    def ricorsione(self, n, film_totali, serata_corrente, film_selezionati, somma_voti, generi_usati, ultimo_genere):
        if len(film_selezionati) == n:
            if len(generi_usati) >= 3 and max(generi_usati.values()) <= 2:
                if 'Comedy' in generi_usati:
                    if generi_usati['Comedy'] >= 2:
                        if  self.migliore_media_programma is None or somma_voti > self.migliore_media_programma:
                            self.miglior_programma = copy.deepcopy(film_selezionati)
                            self.migliore_media_programma = somma_voti
        else:
            for film in film_totali:
                if film.serata == serata_corrente and film.genere != ultimo_genere and (film.genere not in generi_usati or generi_usati[film.genere] < 2):
                    film_selezionati.append(film)
                    if film.genere in generi_usati:
                        generi_usati[film.genere] += 1
                    else:
                        generi_usati[film.genere] = 1
                    somma_voti += (film.somma_voti/film.numero_voti)
                    self.ricorsione(n, film_totali, serata_corrente + 1, film_selezionati, somma_voti, generi_usati, film.genere)
                    somma_voti -= (film.somma_voti/film.numero_voti)
                    generi_usati[film.genere] -= 1
                    if generi_usati[film.genere] == 0:
                        generi_usati.pop(film.genere)
                    film_selezionati.pop()




