import cgi
import os
from tpl import TemplateMaker
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from uccal import data

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
			groupId = self.request.get('groupId')
			member_id = self.request.get('')#<-----------------insert memberid
			Groups.addGroupMember(groupId, member_id)
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

"""class Login(webapp.RequestHandler):
    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        username = self.request.get('username')
        password = self.request.get('password')
        config=open('login.config')
        proper_username=data.ADMIN_EMAIL
        proper_password=data.ADMIN_PASSWORD
        if username != proper_username:
            self.response.out.write('incorrect username.')
        elif password != proper_password:
            self.response.out.write('incorrect password')
        else:
            try :
                self.response.out.write('ok')
            except Exception, e:
                self.response.out.write(e)
        
    def get(self):
        #todo, load the html template for login form
        TemplateMaker.make( self, "Login", "root/login" )"""
	
#------------------End modules input Handlers--------------#
class Sync(webapp.RequestHandler):
    def get(self):
		from uccal import Students
		from uccal import Groups
		from Database import DB
		self.response.headers['Content-Type'] = 'text/plain'
		try :
			Students.sync()
			self.response.out.write('ok')
		except Exception, e:
			self.response.out.write(e)
			
class Test(webapp.RequestHandler):
    def get(self):
		from uccal import Students
		from uccal import Groups
		from Database import DB
		self.response.headers['Content-Type'] = 'text/plain'
		try :
			#user_id = "twj2"
			cal_id = "jeromakay.com_9num3rgpu2b3snt3pp4tfarahc%40group.calendar.google.com"
			group_id = "e38f9ad9371f9fe00d7c3f78b181f814"
			#member_id = "vg2@jeromakay.com"
			#students = Students.getAllMembers()
			#Students.sync()
			#json = DB.ListUsersUIDs()'
			#Groups.addGroupMember(group_id, member_id)
			#Students.subscribe(user_id, cal_id)
			Students.subscribeGroup(group_id, cal_id)
			#ret = Students.getGroupMembers(group_id)
			#self.response.out.write(ret)
			self.response.out.write('ok')
		except Exception, e:
			self.response.out.write(e)
	
#model view controler
application = webapp.WSGIApplication(
									#methods to display pages
                                     [('/', Main),
									 ('/sync', Sync),
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
									  #('/login', Login),
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
	
	
	