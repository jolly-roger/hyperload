import cherrypy

from . import constants

    
def isAuthorized():
    return (bool(cherrypy.session.get(constants.FACEBOOK_ACCESS_TOKEN)) or
        bool(cherrypy.session.get(constants.GOOGLE_ACCESS_TOKEN)))
    
def checkAuthorization():
    if not isAuthorized():
        raise cherrypy.HTTPRedirect("/")