import gdata.apps.groups.client
import data

def adminLogin():
	
	#create client object
	groupClient = gdata.apps.groups.client.GroupsProvisioningClient(domain=data.CONSUMER_KEY) 
	#authorize client
	groupClient.ClientLogin(email=data.ADMIN_EMAIL, password=data.ADMIN_PASSWORD, source ='apps')
	
	return groupClient
	
def adminLogin(type):
	
	if type == "calendar":
		calendar_client = gdata.calendar.client.CalendarClient(source=data.SOURCE_APP_NAME)
		calendar_client.ClientLogin(data.ADMIN_EMAIL, data.ADMIN_PASSWORD, source ='apps')
		return calendar_client