import gdata.apps.groups.client
import data

#---method to update a group---
def updateGroup(group_id, group_name, description='no description given', email_permission=None):

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
	
	newGroupDetail = gdata.apps.groups.data.GroupEntry(group_id, group_name, description)
	
	try :
		#change the group details
		groupClient.UpdateGroup(group_id, newGroupDetail, description, email_permission)
		print "Success!"
		print group_id + " was updated" 
	except Exception :
		print "there was an error with your submission. \nMaybe the group does not exist?"
		