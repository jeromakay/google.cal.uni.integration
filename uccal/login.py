import gdata.apps.groups.client
import data

def adminLogin():

	#---login details to use---
	#TO BE REMOVED
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
	
	return groupClient