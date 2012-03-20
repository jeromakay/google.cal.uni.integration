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
		TemplateMaker.make( self, "Main Page", "root/main" )

#--------Group handlers----------#
class GroupAdder(webapp.RequestHandler):
    def get(self):
        TemplateMaker.make( self, "Add Groups", "groups/add" )
		
class GroupDeleter(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Delete Groups", "groups/delete" )
			
class GroupUpdater(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Update Groups", "groups/update" )
			
class GroupManager(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Manage Groups", "groups/manage" )

		
#--------Module handlers---------#
class ModuleAdder(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Add Modules", "module/add" )

class ModuleDeleter(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Add Modules", "module/delete" )

class ModuleUpdater(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Add Modules", "module/update" )

class AttendanceChecker(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Add Modules", "module/checkAttendance" )

class ModuleManager(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Add Modules", "module/groupManager" )

#--------Students handlers----------#
#---End Page Display Handlers---#

#---Begin Input Handlers---#
class GroupAdderAjax(webapp.RequestHandler):
    def post(self):
		from uccal import Groups
		self.response.headers['Content-Type'] = 'text/plain'
		try :
			groupName = self.request.get('groupName')
			groupDescription = self.request.get('groupDescription')
			Groups.createGroup(groupName, groupDescription)
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
                                      ('/addModule', ModuleAdder),
                                      ('/deleteModule', ModuleDeleter),
                                      ('/updateModule', ModuleUpdater),
                                      ('/moduleManager', ModuleManager),
                                      ('/checkAttendance', AttendanceChecker),
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
	
	
	