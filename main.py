import cgi
import os
from tpl import TemplateMaker
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

#--Begin Page Display Handlers---#
class Main(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Main Page", "main" )

class GroupAdder(webapp.RequestHandler):
    def get(self):
        TemplateMaker.make( self, "Add Groups", "addGroup" )
		
class GroupDeleter(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Delete Groups", "deleteGroup" )
			
class GroupUpdater(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Update Groups", "updateGroup" )
			
class GroupManager(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Manage Groups", "groupManager" )

class ModuleUpdater(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Add Modules", "addModule" )
#---End Page Display Handlers---#

#---Begin Input Handlers---#
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

class GroupManagerAjax(webapp.RequestHandler):
    def post(self):
		#from uccal.groups import update
		self.response.headers['Content-Type'] = 'text/plain'
		try :
			#groupId = self.request.get('groupId')
			#delete.deleteGroup(groupId)
			self.response.out.write('ok')
		except Exception, e:
			self.response.out.write(e)
		
class ModuleUpdaterAjax(webapp.RequestHandler):
    def post(self):
		#from uccal.groups import update
		self.response.headers['Content-Type'] = 'text/plain'
		try :
			#groupId = self.request.get('groupId')
			#delete.deleteGroup(groupId)
			self.response.out.write('ok')
		except Exception, e:
			self.response.out.write(e)
	
#---End input Handlers---#
	
#model view controler
application = webapp.WSGIApplication(
									#methods to display pages
                                     [('/', Main),
                                      ('/addGroup', GroupAdder),
                                      ('/deleteGroup', GroupDeleter),
                                      ('/updateGroup', GroupUpdater),
                                      ('/groupManager', GroupManager),
                                      ('/updateGroup', ModuleUpdater),
									#methods to deal with imput
                                      ('/addGroupAjax', GroupAdderAjax),
									  ('/DeleterAjax', DeleterAjax),
									  ('/updateGroupAjax', GroupUpdaterAjax),
                                      ('/groupManagerAjax', GroupManagerAjax),
									  ('/updateGroupAjax', ModuleUpdaterAjax)],									  
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
	
	
	