import gdata.apps.client
from uccal import login
from uccal import data
from Database import DB

def getAllMembers():
	"""Lists all people in the domain
			
	"""
	
	client = login.adminLogin("student")
	
	Users = client.RetrieveAllUsers()
	for entry in Users.entry:
		users_ret.append(entry.title.text)
	return users_ret

def sync():

	gid = ""
	uid = ""
	
	client = login.adminLogin("student")
	
	Users = client.RetrieveAllUsers()
	for entry in Users.entry:
		name = entry.title.text + " lastname"
		gid =  entry.title.text + "@" + data.CONSUMER_KEY
		uid = entry.title.text		
		DB.CreateUser( gid, uid, name )