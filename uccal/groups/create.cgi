import gdata.apps.groups.client
import data

def createGroup (group_id, group_name, description='no description given', email_permission=None):
	"""Creates a Google Group

		Args:
			group_id: A unique ID to refer to the group
			group_name: A name for the group
			description: describes the group
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
	print groupClient

	try :
		#create the group and add it to the domain
		groupClient.CreateGroup(group_id, group_name, description, email_permission)
		print "Success!"
		print group_name + " was added to " + CONSUMER_KEY + " with the ID " + group_id 
	except Exception :
		print "there was an error with your submission. \nMaybe a group with that ID already Exists?"