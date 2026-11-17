from database.DB_connect import DBConnect
from model.film import Film

class Dao:
    def get_statistiche(n):
        cnx = DBConnect.get_connection()
        try:
            cursor = cnx.cursor()
            try:
                cursor.execute('''SELECT genere, COUNT(*) as numero, SUM(somma_voti ) / SUM(numero_voti ) as media
                                  FROM film
                                  WHERE serata <= %s 
                                  GROUP BY genere ''',(n,))

                result = []
                for r in cursor:
                    result.append(r)
                return result

            finally:
                cursor.close()
        finally:
            cnx.close()

    def get_film(n):
        cnx = DBConnect.get_connection()
        try:
            cursor = cnx.cursor(dictionary=True)
            try:
                cursor.execute('''SELECT *
                                  FROM film 
                                  WHERE serata <= %s 
                                  ORDER BY serata''', (n,))

                result = []
                for r in cursor:
                    film = Film(r['id'], r['titolo'], r['genere'], r['serata'], r['numero_voti'],
                                float(r['somma_voti']))
                    result.append(film)
                return result

            finally:
                cursor.close()
        finally:
            cnx.close()

