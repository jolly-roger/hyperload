import cherrypy
import os.path


class hyperload(object):
    @cherrypy.expose
    def index(self, statusid = 0, *args, **kwargs):
        return "hello"
    
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
        
        raise cherrypy.HTTPRedirect("/")


hyperloadconf = os.path.join(os.path.dirname(__file__), "hyperload.conf")

cherrypy.quickstart(hyperload(), config=hyperloadconf)