from . import base
from . import constants

class user(base.base):
    def __init__(self):
        base.base.__init__(self)
    
    def addFbUser(self, userId):
        self.cur.callproc("addfbuser", [userId])
        self.conn.commit()
        
    def addGglUser(self, userId):
        self.cur.callproc("addggluser", [userId])
        self.conn.commit()