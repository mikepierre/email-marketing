import cherrypy
import os
import json
import time
from jinja2 import Environment, FileSystemLoader

#declare jinja template path
base_dir = os.path.dirname(os.path.abspath(__file__))
j2_env = Environment(loader=FileSystemLoader(base_dir))

class Main:
    def index(self):
    	return "hellow World"
    index.exposed = True


root = Main()

siteconf = os.path.join(os.path.dirname(__file__), 'site.conf')

if __name__ == '__main__':
    cherrypy.quickstart(root, config=siteconf)
else:
    cherrypy.tree.mount(root, config=siteconf)