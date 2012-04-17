import cherrypy

from auth import authorization
from auth import constants

from layout import layout


def isAuthorized(f):
    def _isAuthorized(*args, **kwargs):
        if cherrypy.session.get(constants.IS_SIGNED_REQUEST) is None or cherrypy.session.get(constants.IS_SIGNED_REQUEST) == False:
            cherrypy.session[constants.IS_SIGNED_REQUEST] = False
            
            for kw in kwargs:
                if kw == constants.IS_SIGNED_REQUEST:
                    cherrypy.session[constants.IS_SIGNED_REQUEST] = True
                    break
        
        if cherrypy.session.get(constants.IS_SIGNED_REQUEST):
            if not authorization.isAuthorized():
                authorization.authorize();
            
            return f(*args, **kwargs)
        else:
            if not authorization.isAuthorized():
                return layout.getIndex()
            else:
                authorization.checkAuthorization()
                
                return f(*args, **kwargs)
            
    return _isAuthorized