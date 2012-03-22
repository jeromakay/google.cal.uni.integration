import gdata.apps.client
import gdata.gauth
import gdata.apps.groups.client
import gdata.calendar.client
import atom.data
import gdata.calendar_resource
import string
from uccal import login
from uccal import data
from Database import DB

def getAllMembers():
	"""Lists all people in the domain
			
	"""
	
	client = login.adminLogin("student")
	
	Users = client.RetrieveAllUsers()
	for entry in Users.entry:
		users_ret.append(entry.title.text + " lastname" + "("+ entry.title.text + "@" + data.CONSUMER_KEY +")")
	return users_ret
	
def getGroupMembers(group_id):
	
	client = login.adminLogin()
	
	user_list = []
	
	feed = client.RetrieveAllMembers(group_id)
	for entry in feed.entry:
		member_id = append(entry.GetMemberId())
		member_id = string.replace(member_id, "@jeromakay.com", "")
		user_list.append(member_id)
	return member_id
	
def subscribe( user_id, cal_id ):
	
	calendar_client = login.adminLogin("2legstudent", user_id)
	
	calendar = gdata.calendar.data.CalendarEntry()
	calendar.id = atom.data.Id(text=cal_id)
	returned_calendar = calendar_client.InsertCalendarSubscription(calendar)

def subscribeGroup(group_id, cal_id):

	client = login.adminLogin()
	
	user_list = []
	
	feed = client.RetrieveAllMembers(group_id)
	for entry in feed.entry:
		member_id= (entry.GetMemberId())
		member_id = string.replace(member_id, "@jeromakay.com", "")
		user_list.append(member_id)
	for i in user_list:
		subscribe(i, cal_id)
	

def sync():

	gid = ""
	uid = ""
	
	client = login.adminLogin("student")
	
	Users = client.RetrieveAllUsers()
	
	existing_users = DB.ListUsersUIDs()
	
	for entry in Users.entry:
		name = entry.title.text + " lastname"
		gid =  entry.title.text + "@" + data.CONSUMER_KEY
		uid = entry.title.text	
		if uid not in existing_users:
			DB.CreateUser( gid, uid, name )