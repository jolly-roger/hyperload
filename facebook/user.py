import cherrypy
import urllib.request
import json

from . import constants


USER_URL = "https://graph.facebook.com/me"
FACEBOOK_USER_ID = "facebook_user_id"


def loadUser(userID):
    #raw_user_data = str(urllib.request.urlopen(USER_URL + "?" \
    #    "access_token=" + access_token + \
    #    "&fields=id").read(), encoding="utf-8")
    #
    #user_data = json.loads(raw_user_data)
    #
    #cherrypy.session[FACEBOOK_USER_ID] = user_data['id']
    cherrypy.session[FACEBOOK_USER_ID] = userID
    
def getUserId():
    return cherrypy.session.get(FACEBOOK_USER_ID)
    
def unloadUser():
    cherrypy.lib.sessions.expire()