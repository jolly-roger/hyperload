import cherrypy
import json


import dal.resource
import facebook.user


from isAuthorized import isAuthorized


class resources(object):
    @cherrypy.expose
    @isAuthorized
    def add(self, alias=None, domain=None):
        resourceId = -1
        
        if alias is not None and not alias == "" and domain is not None and not domain == "":
            r = dal.resource.resource()
            resourceId = r.add(alias, domain, facebook.user.getUserId())
            r.close()

        return str(resourceId)
            
    @cherrypy.expose
    @isAuthorized
    def getuserall(self):
        r = dal.resource.resource()
        resources = r.getuserall(facebook.user.getUserId())
        r.close()
        
        return  json.dumps(resources)
        
    @cherrypy.expose
    @isAuthorized
    def verify(self, resourceId):
        pass
    
    @cherrypy.expose
    @isAuthorized
    def getverificationfile(self, resourceId):
        #cherrypy.response.headers['Content-Disposition'] = "attachment"
        
        r = dal.resource.resource()
        resource = r.get(resourceId)
        r.close()
        
        return resource[0][4]