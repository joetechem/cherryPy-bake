# cherryPy-bake
CherryPy as CMF

# CherryPy is     

* A minimalist Python Web Framework  

#### hello-cherrypy.py  

```python  
import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"

cherrypy.quickstart(HelloWorld())
```  

* A Pythonic, Object-Oriented Web Framework  
  - allowing you to build web applications in a similar way to how you'd build any other OO Python program.  
  - Less source code, developed in less time. 
