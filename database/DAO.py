from database.DB_connect import DBConnect
from model.Contiguity import Contiguity
from model.Country import Country


class DAO():
    @staticmethod
    def getAllCountry():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary = True)

        query = """select *
                    from country"""
        cursor.execute(query)

        for row in cursor:
            result.append(Country(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary = True)

        query = """select *
                    from contiguity """
        cursor.execute(query)

        for row in cursor:
            result.append(Contiguity(**row))
        cursor.close()
        conn.close()
        return result

