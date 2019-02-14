"""
Track User Activity (commit 34209f87b70ecfa8d11040cb5bbd54b19fafea48)
- go to http://localhost:8080/
- input a number, this will generate a random string (as before)
- http://localhost:8080/display to see the string

Functionality & UI
- HTML code update to link to a stylesheet
- add the new static resources to the configuration
http://localhost:8080/
"""

import os, os.path
import random
import string

import cherrypy


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head>
          <link href="/static/css/style.css" rel="stylesheet">
          </head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="8" name="length" />
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, length=8):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = some_string
        return some_string

    @cherrypy.expose
    def display(self):
        return cherrypy.session['mystring']


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
          'tools.staticdir.on': True,
          'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)
