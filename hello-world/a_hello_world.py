"""
Most basic CherryPy app
"""
import os.path
import cherrypy

class HelloWorld:
    """Sample request handler class."""

    # Expose the index method through the web.
    # CherryPy will never publish methods that
    # don't have the exposed attribute set to True.
    @cherrypy.expose
    def index(self):
        # CherryPy will call this method for the root URI ("/") and
        # send its return value to the client.
        return 'Hello World'

tutconf = os.path.join(os.path.dirname(__file__), 'helloworld.conf')

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root.
    # A request to '/' will be mapped to HelloWorld().index()
    cherrypy.quickstart(HelloWorld(), config=tutconf)
