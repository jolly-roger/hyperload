import psycopg2

from . import constants


class base(object):
    def __init__(self):
        self.conn = psycopg2.connect(constants.DB_CONNECTION)
        self.cur = self.conn.cursor()
    
    def close(self):
        self.cur.close()
        self.conn.close()