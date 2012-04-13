import cherrypy

from jinja2 import Environment, FileSystemLoader

from facebook import constants as facebookConstatns


env = Environment(loader = FileSystemLoader(cherrypy.request.app.config["hyperload"]["base_dir"] + \
    "layout/templates"))


def getIndex():
    tmpl = env.get_template("pages/index.html")
    return tmpl.render()
    
def getLogin():
    tmpl = env.get_template("pages/login.html")
    return tmpl.render()
    
def getHome():
    tmpl = env.get_template("pages/home.html")
    return tmpl.render()
