import cherrypy


import facebook.user
from facebook import authorization
from facebook import constants as facebookConstatns


import dal.user


class auth(object):
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