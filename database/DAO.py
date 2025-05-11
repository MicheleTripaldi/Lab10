from database.DB_connect import DBConnect
from model.Contiguity import Contiguity
from model.Country import Country


class DAO():
    @staticmethod
    def getAllCountry():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary = True)

        query = """select * from country"""
        cursor.execute(query)

        for row in cursor:
            result.append(Country(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getCountry(anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """select distinct ca.StateAbb, ca.CCode, ca.StateNme
                       from countries.contiguity c, countries.country ca
                       where c.`year` <= %s
                        and c.state1no = ca.CCode"""
        cursor.execute(query, (anno,))

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

