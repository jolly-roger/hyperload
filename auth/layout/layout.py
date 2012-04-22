import cherrypy

from jinja2 import Environment, FileSystemLoader


env = None


def getenv():
    global env
    
    if env is None:
        env = Environment(loader = FileSystemLoader(cherrypy.request.app.config["hyperload"]["base_dir"] + \
            "auth/layout/templates"))
        
    return env
    
def getGglCallbackHandler():
    tmpl = getenv().get_template("pages/gglCallbackHandler.html")
    return tmpl.render()