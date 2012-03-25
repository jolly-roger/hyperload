import cherrypy
import constants

from jinja2 import Environment, FileSystemLoader

from facebook import constants as facebookConstatns


env = Environment(loader = FileSystemLoader(constants.BASE_DIR + "layout/templates"))


def getIndex():
    tmpl = env.get_template("pages/index.html")
    return tmpl.render()
    
def getLogin():
    tmpl = env.get_template("pages/login.html")
    return tmpl.render()
