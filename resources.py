import cherrypy
import json
import urllib.request

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
        isVerified = False
        r = dal.resource.resource()
        resource = r.get(int(resourceId))
        
        verificationData = str(urllib.request.urlopen(resource[0][2] + "/hyperload.txt").read(), encoding="utf-8")
        
        if verificationData == resource[0][4]:
            r.verify(resourceId)
            isVerified = True
            
        r.close()
        
        if isVerified:
            return 1
        else:
            return 0
    
    @cherrypy.expose
    @isAuthorized
    def getverificationfile(self, resourceId):
        cherrypy.response.headers['Content-Disposition'] = "attachment; filename=hyperload.txt"
        
        r = dal.resource.resource()
        resource = r.get(int(resourceId))
        r.close()
        
        return resource[0][4]
        
    @cherrypy.expose
    @isAuthorized
    def remove(self, resourceId):
        r = dal.resource.resource()
        r.remove(resourceId)
        r.close()