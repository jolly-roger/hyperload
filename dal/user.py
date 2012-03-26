from . import base
from . import constants

class user(base.base):
    def __init__(self):
        base.base.__init__(self)
    
    def addFbUser(self, fbUserId):
        self.cur.execute(constants.ADD_FB_USER, {"fbuserid": fbUserId})
        self.conn.commit()