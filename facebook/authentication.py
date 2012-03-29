import cherrypy
import urllib.request
import urllib.parse

from . import constants
from . import user


def authenticate(code):
    #req = urllib.request.Request("https://graph.facebook.com/oauth/access_token?" \
    #    "client_id=" + constants.APP_ID  + "&redirect_uri=" + constants.AUTHORIZE_CALLBACK_URL + \
    #    "&client_secret=" + constants.APP_SECRET + "&code=" + code,
    #    headers={"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:11.0) Gecko/20100101 Firefox/11.0"})
    #raw_access_data = str(urllib.request.urlopen(req).read(), encoding="utf-8")
        
    raw_access_data = str(urllib.request.urlopen("https://graph.facebook.com/oauth/access_token?" \
        "client_id=" + constants.APP_ID  + "&redirect_uri=" + constants.AUTHORIZE_CALLBACK_URL + \
        "&client_secret=" + constants.APP_SECRET + "&code=" + code).read(), encoding="utf-8")
    
    access_data = urllib.parse.parse_qs(raw_access_data)
    
    cherrypy.session[constants.FACEBOOK_ACCESS_TOKEN] = access_data['access_token'][0]
    #cherrypy.session[constants.FACEBOOK_ACCESS_TOKEN]['expires'] = access_data['expires'][0]
    
    user.loadUser(access_data['access_token'][0])

#def authenticate(code):
#    raise cherrypy.HTTPRedirect("https://graph.facebook.com/oauth/access_token?" \
#        "client_id=" + constants.APP_ID + "&redirect_uri=" + constants.AUTHORIZE_CALLBACK_URL + \
#        "&client_secret=" + constants.APP_SECRET + "&code=" + code)
#    
#def callbackHandler():    
#    access_data = urllib.parse.parse_qs(raw_access_data)
#    
#    cherrypy.session[constants.FACEBOOK_ACCESS_TOKEN] = access_data['access_token'][0]
#    #cherrypy.session[constants.FACEBOOK_ACCESS_TOKEN]['expires'] = access_data['expires'][0]
#    
#    user.loadUser(access_data['access_token'][0])



