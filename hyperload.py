import cherrypy
import os.path
import constants

from isAuthorized import isAuthorized

from facebook import authorization
from facebook import authentication
from facebook import user
from facebook import constants as facebookConstatns

from layout import layout


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
        user.unloadUser()
        
        raise cherrypy.HTTPRedirect("/")
    
    @cherrypy.expose
    def login(self):
        authorization.authorize();        

    @cherrypy.expose
    def authorizecallback(self, code=None, error_reason=None, error=None):
        authorization.callbackHandler(code)
        authentication.authenticate(code)
        
        raise cherrypy.HTTPRedirect("/home")


hyperloadconf = os.path.join(os.path.dirname(__file__), "hyperload.conf")

cherrypy.quickstart(hyperload(), config=hyperloadconf)