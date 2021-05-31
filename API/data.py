import psycopg2

class DataAccess:
    
    @classmethod
    def connexion(cls):
        cls.conn = psycopg2.connect(host="postgre.c893joqbrj9g.us-east-2.rds.amazonaws.com",
                                    port="5432",
                                    database="exercises",
                                    user="master",
                                    password="motdepasse")
        cls.cur = cls.conn.cursor()

    @classmethod
    def requete_1(cls):
        cls.cur.execute("select * from cd.facilities;")
        resultat = list(cls.cur)
        return resultat

    @classmethod
    def requete_2(cls):
        cls.cur.execute("select name, membercost from cd.facilities;")
        resultat = list(cls.cur)
        return resultat

    @classmethod
    def deconnexion(cls):
        cls.conn.close()