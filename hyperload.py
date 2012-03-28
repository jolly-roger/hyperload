import cherrypy
import os.path
import constants
import json

from isAuthorized import isAuthorized

from facebook import authorization
from facebook import authentication
from facebook import constants as facebookConstatns

import facebook.user

from layout import layout

import dal.user
import dal.resource


class hyperload(object):
    @cherrypy.expose
    def index(self, statusid = 0, *args, **kwargs):
        return layout.getIndex()
        
    @cherrypy.expose
    @isAuthorized
    def home(self):
        return layout.getHome()
    
    @cherrypy.expose
    def logout(self):
        authorization.checkAuthorization()
        facebook.user.unloadUser()
        
        raise cherrypy.HTTPRedirect("/")
    
    @cherrypy.expose
    def login(self):
        authorization.authorize();        

    @cherrypy.expose
    def authorizecallback(self, code=None, error_reason=None, error=None):
        if code is not None:
            authorization.callbackHandler(code)
            authentication.authenticate(code)
        
    @cherrypy.expose
    def authenticatecallback(self, rawaccessdata=None):
        if rawaccessdata is not None and not rawaccessdata == "":
            authentication.callbackHandler(rawaccessdata)
            
            u = dal.user.user()
            u.addFbUser(facebook.user.getUserId())
            u.close()
        
        raise cherrypy.HTTPRedirect("/home")
        
        #return "hello :)"
    
    @cherrypy.expose
    @isAuthorized
    def addresource(self, alias=None, domain=None):
        if alias is not None and not alias == "" and domain is not None and not domain == "":
            r = dal.resource.resource()
            r.add(alias, domain, facebook.user.getUserId())
            r.close()
            
    @cherrypy.expose
    @isAuthorized
    def getresources(self):
        r = dal.resource.resource()
        resources = r.get(facebook.user.getUserId())
        r.close()
        
        return  json.dumps(resources)
        
    @cherrypy.expose
    @isAuthorized
    def verifyresource(self):
        pass


hyperloadconf = os.path.join(os.path.dirname(__file__), "hyperload.conf")

cherrypy.quickstart(hyperload(), config=hyperloadconf)