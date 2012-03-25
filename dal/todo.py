from . import base
from . import constants

class todo(base.base):
    def __init__(self):
        base.base.__init__(self)    
    
    def add(self, userid, name):
        self.cur.execute(constants.ADD_TODO, {"todoname": name, "userid": userid})
        self.conn.commit()
        
    def share(self, todoid, friendid):
        self.cur.execute(constants.SHARE_TODO, {"todoid": todoid, "friendid": friendid})
        self.conn.commit()
    
    def setpriority(self, todoid, todopriority):
        self.cur.execute(constants.SET_PRIORITY, {"todoid": todoid, "todopriority": todopriority})
        self.conn.commit()
    
    def setstatus(self, todoid, statusid):
        self.cur.execute(constants.SET_STATUS, {"todoid": todoid, "statusid": statusid})
        self.conn.commit()