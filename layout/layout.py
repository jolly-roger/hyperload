import cherrypy

from jinja2 import Environment, FileSystemLoader

from facebook import constants as facebookConstatns


env


def getenv():
    if not env:
        env = Environment(loader = FileSystemLoader(cherrypy.request.app.config["hyperload"]["base_dir"] + \
            "layout/templates"))
        
    return env

def getIndex():
    tmpl = getenv().get_template("pages/index.html")
    return tmpl.render()
    
def getLogin():
    tmpl = getenv().get_template("pages/login.html")
    return tmpl.render()
    
def getHome():
    tmpl = getenv().get_template("pages/home.html")
    return tmpl.render()
