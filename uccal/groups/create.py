import gdata.apps.groups.client
from uccal import data
import random
import hashlib
from uccal import login
#from Database import CreateGroup

def createGroup (group_name, description='no description given', type_id=1, email_permission=None):
	"""Creates a Google Group with the given paramaters 

		Args:
			group_name: A name for the group
			description: describes the group
			type_id: The type of members of the group (eg student, staff) represented by an int (see database documentation)
			email_permission: Email settings for the group. 
	"""

	#generate hashed id
	group_id = hashlib.md5(group_name).hexdigest()
	
	#deal with database here
	#CreateGroup.CreateGroup(Database, group_Name, description, group_id, type_id)
	
	#create client object
	groupClient = login.adminLogin()

	#create the group and add it to the domain
	groupClient.CreateGroup(group_id, group_name, description, email_permission)
