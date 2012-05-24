from . import base

import cherrypy


class job(base.base):
    def __init__(self):
        base.base.__init__(self)
    
    def add(self, alias, resourceId):
        self.cur.callproc("addjob", [alias, resourceId])
        self.conn.commit()
        result = self.cur.fetchall()
        
        return result[0][0]
        
    def getresourceall(self, resourceId):
        self.cur.callproc("getjobs", [resourceId])
        
        return self.cur.fetchall()
        
    def get(self, jobId):
        self.cur.callproc("getjob", [jobId])
        
        return self.cur.fetchall()
        
    def remove(self, jobId):
        self.cur.callproc("removejob", [jobId])
        self.conn.commit()