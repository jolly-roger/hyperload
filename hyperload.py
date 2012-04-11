import cherrypy
import os.path
import constants
import json
import urllib.request

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
    def login(self, accessToken = None, expiresIn = None, signedRequest = None, userID = None):
        if accessToken is not None:
            cherrypy.session[facebookConstatns.FACEBOOK_ACCESS_TOKEN] = accessToken
            facebook.user.loadUser(userID)
            
            u = dal.user.user()
            u.addFbUser(facebook.user.getUserId())
            u.close()
            
        return "/home"
    
    
    
    
    
    @cherrypy.expose
    #@isAuthorized
    def addresource(self, alias=None, domain=None):
        #resourceId = -1
        
        #if alias is not None and not alias == "" and domain is not None and not domain == "":
            #r = dal.resource.resource()
            #resourceId =
            #r.add(alias, domain, facebook.user.getUserId())
            #r.close()
            
            #pass
            
            #cherrypy.log.error(str(resourceId))
            
        #return str(resourceId)
        
        return ""
            
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