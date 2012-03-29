import cherrypy
import urllib.request
import urllib.parse

from . import constants
from . import user


#def authenticate(code):
#    #req = urllib.request.Request("https://graph.facebook.com/oauth/access_token?" \
#    #    "client_id=" + constants.APP_ID  + "&redirect_uri=" + constants.AUTHORIZE_CALLBACK_URL + \
#    #    "&client_secret=" + constants.APP_SECRET + "&code=" + code,
#    #    headers={"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:11.0) Gecko/20100101 Firefox/11.0"})
#    #raw_access_data = str(urllib.request.urlopen(req).read(), encoding="utf-8")
#    
#    
##    import urllib.request
##>>> import urllib.parse
##>>> params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
##>>> f = urllib.request.urlopen("http://www.musi-cal.com/cgi-bin/query?%s" % params)
#    
#    params = urllib.parse.urlencode({"client_id": constants.APP_ID, "redirect_uri": constants.AUTHORIZE_CALLBACK_URL,
#        "client_secret": constants.APP_SECRET, "code": code})
#    
#    raw_access_data = str(urllib.request.urlopen("https://graph.facebook.com/oauth/access_token?%s" % params).read(),
#        encoding="utf-8")
#        
#    #raw_access_data = str(urllib.request.urlopen("https://graph.facebook.com/oauth/access_token?" \
#    #    "client_id=" + constants.APP_ID  + "&redirect_uri=" + constants.AUTHORIZE_CALLBACK_URL + \
#    #    "&client_secret=" + constants.APP_SECRET + "&code=" + code).read(), encoding="utf-8")
#    
#    access_data = urllib.parse.parse_qs(raw_access_data)
#    
#    cherrypy.session[constants.FACEBOOK_ACCESS_TOKEN] = access_data['access_token'][0]
#    #cherrypy.session[constants.FACEBOOK_ACCESS_TOKEN]['expires'] = access_data['expires'][0]
#    
#    user.loadUser(access_data['access_token'][0])

def authenticate(code):
    params = urllib.parse.urlencode({"client_id": constants.APP_ID, "redirect_uri": constants.AUTHORIZE_CALLBACK_URL,
        "client_secret": constants.APP_SECRET, "code": code})
    
    req = urllib.request.Request("https://graph.facebook.com/oauth/access_token?%s" % params,
        headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-us,en;q=0.7,ru;q=0.3",
            "Connection": "keep-alive",
            "Host": "graph.facebook.com",
            "Referer": "http://dig-dns.com/",
            "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:11.0) Gecko/20100101 Firefox/11.0"})    
    
    #raise cherrypy.HTTPRedirect()
    
    return urllib.request.urlopen(req).read()
    
    #raw_access_data = str(urllib.request.urlopen("https://graph.facebook.com/oauth/access_token?%s" % params).read(),
    #    encoding="utf-8")
    
def callbackHandler(raw_access_data):    
    access_data = urllib.parse.parse_qs(raw_access_data)
    
    cherrypy.session[constants.FACEBOOK_ACCESS_TOKEN] = access_data['access_token'][0]
    #cherrypy.session[constants.FACEBOOK_ACCESS_TOKEN]['expires'] = access_data['expires'][0]
    
    user.loadUser(access_data['access_token'][0])



