import cherrypy
import os.path
import constants

from isAuthorized import isAuthorized

from facebook import authorization
from facebook import constants as facebookConstatns

import facebook.user

from layout import layout

import dal.user

import resources


class hyperload(object):
    resources = resources.resources()
    
    
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
        
        return "/"
        
    @cherrypy.expose
    def login(self, accessToken = None, expiresIn = None, signedRequest = None, userID = None):
        if accessToken is not None:
            cherrypy.session[facebookConstatns.FACEBOOK_ACCESS_TOKEN] = accessToken
            facebook.user.loadUser(userID)
            
            u = dal.user.user()
            u.addFbUser(facebook.user.getUserId())
            u.close()
            
        return "/home"


hyperloadconf = os.path.join(os.path.dirname(__file__), "hyperload.conf")

cherrypy.quickstart(hyperload(), config=hyperloadconf)