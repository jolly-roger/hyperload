import cherrypy
import urllib.request
import json

from . import constants
from . import loginTypes


USER_ID = "user_id"
LOGIN_TYPE = "login_type"


def loadUser(userID, loginType):
    cherrypy.session[USER_ID] = userID
    cherrypy.session[LOGIN_TYPE] = loginType
    
def getUserId():
    return cherrypy.session.get(USER_ID)
    
def getLoginType():
    return cherrypy.session.get(LOGIN_TYPE)
    
def unloadUser():
    cherrypy.lib.sessions.expire()