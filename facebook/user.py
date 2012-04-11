import cherrypy
import urllib.request
import json

from . import constants


FACEBOOK_USER_ID = "facebook_user_id"


def loadUser(userID):
    cherrypy.session[FACEBOOK_USER_ID] = userID
    
def getUserId():
    return cherrypy.session.get(FACEBOOK_USER_ID)
    
def unloadUser():
    cherrypy.lib.sessions.expire()