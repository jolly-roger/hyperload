from . import base
from . import constants

class resource(base.base):
    def __init__(self):
        base.base.__init__(self)
    
    def add(self, name, outerUserId):
        self.cur.execute(constants.ADD_RESOURCE, {"resourcename": name, "outeruserid": outerUserId})
        self.conn.commit()