import cherrypy
import json
import urllib.request

import dal.job
import auth.user


from auth import isAuthorized as authorization


class jobs(object):
    @cherrypy.expose
    @authorization.isAuthorized
    def add(self, alias=None, resourceId=None):
        jobId = -1
        
        if alias is not None and not alias == "" and resourceId is not None:
            j = dal.job.job()
            jobId = j.add(alias, resourceId)
            j.close()

        return str(jobId)
            
    @cherrypy.expose
    @authorization.isAuthorized
    def getuserall(self, resourceId=None):
        jobs = []
        
        if resourceId is not None:
            j = dal.job.job()
            jobs = j.getuserall(resourceId)
            j.close()
        
        return  json.dumps(jobs)
        
    @cherrypy.expose
    @authorization.isAuthorized
    def remove(self, jobId):
        j = dal.job.job()
        j.remove(jobId)
        j.close()