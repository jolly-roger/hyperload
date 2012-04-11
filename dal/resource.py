from . import base
from . import constants

import cherrypy


class resource(base.base):
    def __init__(self):
        base.base.__init__(self)
    
    def add(self, alias, domain, outerUserId):
        self.cur.execute(constants.ADD_RESOURCE, {"resourcealias": alias, "resourcedomain": domain,
            "outeruserid": outerUserId})
        self.conn.commit()

        return self.cur.fetchall()[0][0]
        
    def get(self, outerUserId):
        self.cur.execute(constants.GET_RESOURCES, {"outeruserid": outerUserId})
        
        return self.cur.fetchall()