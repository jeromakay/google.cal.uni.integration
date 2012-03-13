import cgi
import os
from tpl import TemplateMaker
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
		except Exception, e:
			self.response.out.write(e)
		
class GroupDeleter(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Delete Groups", "deleteGroup" )
		
class DeleterAjax(webapp.RequestHandler):
    def post(self):
		from uccal import Deleters
		self.response.headers['Content-Type'] = 'text/plain'
		try :
			entityID = self.request.get('entityID')
			dataType = self.request.get('dataType')
			Deleters.Delete(dataType, entityID)
			self.response.out.write('ok')
		except Exception, e:
			self.response.out.write(e)
			
class GroupUpdater(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Update Groups", "updateGroup" )
		
class GroupUpdaterAjax(webapp.RequestHandler):
    def post(self):
		from uccal.groups import update
		self.response.headers['Content-Type'] = 'text/plain'
		try :
			groupId = self.request.get('groupId')
			#delete.deleteGroup(groupId)
			self.response.out.write('ok')
		except Exception, e:
			self.response.out.write(e)

class ModuleUpdater(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Add Modules", "addModule" )
		
class ModuleUpdaterAjax(webapp.RequestHandler):
    def post(self):
		from uccal.groups import update
		self.response.headers['Content-Type'] = 'text/plain'
		try :
			#groupId = self.request.get('groupId')
			#delete.deleteGroup(groupId)
			self.response.out.write('ok')
		except Exception, e:
			self.response.out.write(x)
	

application = webapp.WSGIApplication(
                                     [('/', Main),
                                      ('/addGroupAjax', GroupAdderAjax),
                                      ('/addGroup', GroupAdder),
									  ('/DeleterAjax', DeleterAjax),
                                      ('/deleteGroup', GroupDeleter),
									  ('/updateGroupAjax', GroupUpdaterAjax),
                                      ('/updateGroup', GroupUpdater),
									  ('/updateGroupAjax', ModuleUpdaterAjax),
                                      ('/updateGroup', ModuleUpdater)],									  
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
	
	
	