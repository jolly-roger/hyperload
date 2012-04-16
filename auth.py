import cherrypy
import urllib.request

import facebook.user
from facebook import authorization
from facebook import constants as facebookConstants
from facebook import loginTypes

import dal.user

from layout import layout


class auth(object):
    @cherrypy.expose
    def logout(self):
        authorization.checkAuthorization()
        facebook.user.unloadUser()
        
        return "/"
        
    @cherrypy.expose
    def fblogin(self, accessToken = None, expiresIn = None, signedRequest = None, userID = None):
        if accessToken is not None:
            cherrypy.session[facebookConstants.FACEBOOK_ACCESS_TOKEN] = accessToken
            facebook.user.loadUser(userID, loginTypes.Facebook)
            
            u = dal.user.user()
            u.addFbUser(facebook.user.getUserId())
            u.close()
            
        return "/home"
    
    @cherrypy.expose
    def ggllogin(self, accessToken = None):#, userID = None):
        if accessToken is not None:
            cherrypy.session[facebookConstants.GOOGLE_ACCESS_TOKEN] = accessToken
            
            
            urllib.request.urlopen("https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=" + accessToken)
            
            
            
            #facebook.user.loadUser(userID, loginTypes.Google)
            
            #u = dal.user.user()
            #u.addGglUser(facebook.user.getUserId())
            #u.close()
            
        return "/home"
    
    
    @cherrypy.expose
    def gglcallbackhandler(self):
        return layout.getGglCallbackHandler()