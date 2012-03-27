from . import base
from . import constants

class resource(base.base):
    def __init__(self):
        base.base.__init__(self)
    
    def add(self, alias, domain, outerUserId):
        self.cur.execute(constants.ADD_RESOURCE, {"resourcealias": alias, "resourcedomain": domain,
            "outeruserid": outerUserId})
        self.conn.commit()
        
    def get(self, outerUserId):
        self.cur.execute(constants.GET_RESOURCES, {"outeruserid": outerUserId})
        
        return self.cur.fetchall()