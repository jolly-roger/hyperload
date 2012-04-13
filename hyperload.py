import cherrypy
import os.path

from isAuthorized import isAuthorized

from layout import layout

import resources
import auth


class hyperload(object):
    resources = resources.resources()
    auth = auth.auth()
    
    
    @cherrypy.expose
    def index(self, statusid = 0, *args, **kwargs):
        return layout.getIndex()
        
    @cherrypy.expose
    @isAuthorized
    def home(self):
        return layout.getHome()
        
    @cherrypy.expose
    def js(self):
        cherrypy.response.headers['Content-Type'] = "text/javascript"
        
        js = open(cherrypy.request.app.config["hyperload"]["base_dir"] + "js/common.js", "r").read()
        
        return js


hyperloadconf = os.path.join(os.path.dirname(__file__), "hyperload.conf")

cherrypy.quickstart(hyperload(), config=hyperloadconf)