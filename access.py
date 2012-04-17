import cherrypy
import urllib.request
import json

import auth.user
from auth import authorization
from auth import constants as authConstants
from auth import loginTypes

import dal.user

from layout import layout


class access(object):
    @cherrypy.expose
    def logout(self):
        authorization.checkAuthorization()
        auth.user.unloadUser()
        
        return "/"
        
    @cherrypy.expose
    def fblogin(self, accessToken = None, expiresIn = None, signedRequest = None, userID = None):
        if accessToken is not None:
            cherrypy.session[authConstants.FACEBOOK_ACCESS_TOKEN] = accessToken
            auth.user.loadUser("fb_" + userID, loginTypes.Facebook)
            
            u = dal.user.user()
            u.add(auth.user.getUserId())
            u.close()
            
        return "/home"
    
    @cherrypy.expose
    def ggllogin(self, accessToken = None):
        if accessToken is not None:
            cherrypy.session[authConstants.GOOGLE_ACCESS_TOKEN] = accessToken

            rawData = str(
                urllib.request.urlopen("https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=" + accessToken).
                read(), encoding="utf-8")
            
            data = json.loads(rawData)

            auth.user.loadUser("ggl_" + data["user_id"], loginTypes.Google)
            
            u = dal.user.user()
            u.add(auth.user.getUserId())
            u.close()
            
        return "/home"
    
    
    @cherrypy.expose
    def gglcallbackhandler(self):
        return layout.getGglCallbackHandler()