import gdata.apps.groups.client
import data
import random
import hashlib
#from Database import EditGroup

def updateGroup(group_id, new_group_name, new_description='no description given', new_type_id=1, new_email_permission=None):
	"""Updates a google group with the given paramaters 
	
		Args:
			group_name: A new name for the group
			description: A new description for the group
			type_id: The type of members of the group (eg student, staff) represented by an int (see database documentation)
			email_permission: Email settings for the group.
	"""

	#---login details to use---
	#user id eg abc1
	user = data.ADMIN_ID
	#user email eg abc1@example.com
	user_full = data.ADMIN_EMAIL
	#user password
	password = data.ADMIN_PASSWORD
	#the domain key eg. example.com
	CONSUMER_KEY = data.CONSUMER_KEY

	#create client object
	groupClient = gdata.apps.groups.client.GroupsProvisioningClient(domain=CONSUMER_KEY) 
	#authorize client
	groupClient.ClientLogin(email=user_full, password=password, source ='apps')
	
	#create a new group object to change with the old one.
	#newGroupDetail = gdata.apps.groups.data.GroupEntry(group_id, new_group_name, new_description, new_type_id)
		
	#deal with database here
	#EditGroup.EditGroup(database, group_id, new_group_name, new_description, new_group_type)
	
	#change the group details
	groupClient.UpdateGroup(group_id, newGroupDetail, description, email_permission)
		