from database.dao import Dao

class Model:

    def __init__(self):
        pass
    def get_statistiche_per_genere(self,n):
        statistiche_per_genere = Dao.get_statistiche(n)
        return statistiche_per_genere


