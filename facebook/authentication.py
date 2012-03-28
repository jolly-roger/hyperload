import cherrypy
import urllib.request
import urllib.parse

from . import constants
from . import user


def authenticate(code):
    raw_access_data = str(urllib.request.urlopen("https://graph.facebook.com/oauth/access_token?" \
        "client_id=" + constants.APP_ID  + \
        "&client_secret=" + constants.APP_SECRET + "&code=" + code).read(), encoding="utf-8")
    
    #"&redirect_uri=" + constants.CALLBACK_URL + \
    
    access_data = urllib.parse.parse_qs(raw_access_data)
    
    cherrypy.session[constants.FACEBOOK_ACCESS_TOKEN] = access_data['access_token'][0]
    #cherrypy.session[constants.FACEBOOK_ACCESS_TOKEN]['expires'] = access_data['expires'][0]
    
    user.loadUser(access_data['access_token'][0])



