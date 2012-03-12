import cgi
import os
import TemplateMaker
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class Main(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Main Page", "main" )

class GroupAdder(webapp.RequestHandler):
    def get(self):
        TemplateMaker.make( self, "Add Groups", "addGroup" )
		
class GroupAdderAjax(webapp.RequestHandler):
    def post(self):
		from uccal.groups import create
		self.response.headers['Content-Type'] = 'text/plain'

		try :
			groupName = self.request.get('groupName')
			groupDescription = self.request.get('groupDescription')
			create.createGroup(groupName, groupDescription)
			self.response.out.write('ok')
		except Exception, x:
			self.response.out.write(x)
		
class GroupDeleter(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Delete Groups", "deleteGroup" )
		
class GroupDeleterAjax(webapp.RequestHandler):
    def get(self):
        self.post();
		
    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('ok')
	

application = webapp.WSGIApplication(
                                     [('/', Main),
                                      ('/addGroupAjax', GroupAdderAjax),
                                      ('/addGroup', GroupAdder),
									  ('/deleteGroupAjax', GroupDeleterAjax),
                                      ('/deleteGroup', GroupDeleter)],									  
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
	
	
	