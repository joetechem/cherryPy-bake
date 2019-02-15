# cherryPy-bake
CherryPy as CMF  

[![Build Status](https://travis-ci.org/joetechem/cherryPy-bake.svg?branch=master)](https://travis-ci.org/joetechem/cherryPy-bake)

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

## Organized Code  

CherryPy comes with a useful architecture that helps you organize your code to make it easier to maintain and more flexible.  

Several mechanisms to choose from, here we'll use 3:  
* dispatchers  
* tools  
* plugins  

### Example Scenario  

Imagine you are at a superstore:  
* You have several tills and people queuing for each of them (those are your requests)  
* You have various sections with food and other stuff (these are your data)  
* Finally you have the superstore people and their daily tasks to make sure sections are always in order (this is your backend)  

#### The Dispatchers  
You likely will want to perform operations based on the till:  
* Have a till for baskets with less than ten items  
* Have a till for disabled people  
* Have a till for pregnant women  
* Have a till where you can only using the store card  

To support these use-cases, CherryPy provides a mechanism called a dispatcher. A dispatcher is executed early during the request processing in order to determine which piece of code of your application will handle the incoming request. Or, to continue on the store analogy, a dispatcher will decide which till to lead a customer to.  

#### The Tools  
Let’s assume your store has decided to operate a discount spree but, only for a specific category of customers. CherryPy will deal with such use case via a mechanism called a  tool.  

A tool is a piece of code that runs on a per-request basis in order to perform additional work. Usually a tool is a simple Python function that is executed at a given point during the process of the request by CherryPy.  

#### The Plugins  

As we have seen, the store has a crew of people dedicated to manage the stock and deal with any customers’ expectation.  

In the CherryPy world, this translates into having functions that run outside of any request life-cycle. These functions should take care of background tasks, long lived connections (such as those to a database for instance), etc.  

Plugins are called that way because they work along with the CherryPy engine and extend it with your operations.  


