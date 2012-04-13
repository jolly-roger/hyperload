from . import base
from . import constants

class user(base.base):
    def __init__(self):
        base.base.__init__(self)
    
    def addFbUser(self, fbUserId):
        self.cur.callproc("addfbuser", [fbUserId])
        self.conn.commit()