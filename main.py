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
		TemplateMaker.make( self, "Add Modules", "modules/add" )

class ModuleDeleter(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Delete Modules", "modules/delete" )

class ModuleUpdater(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Update Modules", "modules/update" )

class AttendanceChecker(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Check Module Attendance", "modules/checkAttendance" )

class ModuleManager(webapp.RequestHandler):
    def get(self):
		TemplateMaker.make( self, "Manage Modules/Groups", "modules/groupManager" )

#--------Students handlers----------#
class StudentBrowser(webapp.RequestHandler):
    def get(self):
        TemplateMaker.make( self, "Browse Students", "students/browse" )

class StudentAdder(webapp.RequestHandler):
    def get(self):
        TemplateMaker.make( self, "Add Students", "students/add" )

class StudentErasmus(webapp.RequestHandler):
    def get(self):
        TemplateMaker.make( self, "Erasmus Students", "students/erasmus" )

class StudentRemover(webapp.RequestHandler):
    def get(self):
        TemplateMaker.make( self, "Remove Students", "students/remove" )
		
#---End Page Display Handlers---#

#---Begin Input Handlers---#

#------handles generic deletions------#		
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
			
#---Handles fetching data from database for dropdowns---#
class FetchersAjax(webapp.RequestHandler):
    def post(self):
		from uccal import fetchers
		self.response.headers['Content-Type'] = 'text/plain'
		try :
			dataType = self.request.get('dataType')
			json = fetchers.fetch( dataType )
			self.response.out.write(json)
		except Exception, e:
			self.response.out.write( e )

#------------------Begin groups input handlers-------------#
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
		
class GroupUpdaterAjax(webapp.RequestHandler):
    def post(self):
		from uccal import Groups
		self.response.headers['Content-Type'] = 'text/plain'
		try :
			groupId = self.request.get('groupId')
			groupName = self.request.get('groupName')
			groupDescription = self.request.get('groupDescription')
			Groups.updateGroup(groupId, groupName, groupDescription)
			self.response.out.write('ok')
		except Exception, e:
			self.response.out.write(e)

class GroupManagerAjax(webapp.RequestHandler):
    def post(self):
		from uccal import Groups
		self.response.headers['Content-Type'] = 'text/plain'
		try :
			#groupId = self.request.get('groupId')
			#delete.deleteGroup(groupId)
			self.response.out.write('ok')
		except Exception, e:
			self.response.out.write(e)
#------------------End groups input handlers---------------#

#------------------Begin modules input handlers------------#
class ModuleAdderAjax(webapp.RequestHandler):
    def post(self):
		from uccal import Modules
		self.response.headers['Content-Type'] = 'text/plain'
		try :
			moduleName = self.request.get('moduleName')
			moduleDescription = self.request.get('moduleDescription')
			Modules.addModule(moduleName, moduleDescription)
			self.response.out.write('ok')
		except Exception, e:
			self.response.out.write(e)

class ModuleUpdaterAjax(webapp.RequestHandler):
    def post(self):
		from uccal import Modules
		self.response.headers['Content-Type'] = 'text/plain'
		try :
			#groupId = self.request.get('groupId')
			#delete.deleteGroup(groupId)
			self.response.out.write('ok')
		except Exception, e:
			self.response.out.write(e)
	
#------------------End modules input Handlers--------------#
class Test(webapp.RequestHandler):
    def get(self):
		from uccal import Students
		self.response.headers['Content-Type'] = 'text/plain'
		try :
			#students = Students.getAllMembers()
			ok = Students.sync()
			self.response.out.write(ok)
		except Exception, e:
			self.response.out.write(e)
	
#model view controler
application = webapp.WSGIApplication(
									#methods to display pages
                                     [('/', Main),
									 
									 ('/test', Test),
									#
                                      ('/addGroup', GroupAdder),
                                      ('/deleteGroup', GroupDeleter),
                                      ('/updateGroup', GroupUpdater),
                                      ('/groupManager', GroupManager),
									#
                                      ('/addModule', ModuleAdder),
                                      ('/deleteModule', ModuleDeleter),
                                      ('/updateModule', ModuleUpdater),
                                      ('/moduleGroupManager', ModuleManager),
                                      ('/checkAttendance', AttendanceChecker),									  
                                    #
									  ('/studentBrowser', StudentBrowser),
                                      ('/studentAdder', StudentAdder),
                                      ('/studentErasmus', StudentErasmus),
                                      ('/studentRemover', StudentRemover),
									#methods to deal with input
									  ('/DeleterAjax', DeleterAjax),
									  ('/fetchers', FetchersAjax),
									#
                                      ('/addGroupAjax', GroupAdderAjax),
									  ('/updateGroupAjax', GroupUpdaterAjax),
                                      ('/groupManagerAjax', GroupManagerAjax),
									#
									  ('/AddModuleAjax', ModuleAdderAjax),
									  ('/updateGroupAjax', ModuleUpdaterAjax)
									  #('/AddGroupAjax', ModuleAdderAjax),
									  #('/AddGroupAjax', ModuleAdderAjax),
									  ],									  
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
	
	
	