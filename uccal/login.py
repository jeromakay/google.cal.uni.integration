import gdata.apps.groups.client
import data
	
def adminLogin(type=None):
	
	if type == None:
		#create client object
		groupClient = gdata.apps.groups.client.GroupsProvisioningClient(domain=data.CONSUMER_KEY) 
		#authorize client
		groupClient.ClientLogin(email=data.ADMIN_EMAIL, password=data.ADMIN_PASSWORD, source ='apps')
		return groupClient
	
	if type == "calendar":
		calendar_client = gdata.calendar.client.CalendarClient(source=data.SOURCE_APP_NAME)
		calendar_client.ClientLogin(data.ADMIN_EMAIL, data.ADMIN_PASSWORD, source ='apps')
		return calendar_client
		
	if type == "student":
		
		client = gdata.apps.client.AppsClient(domain=data.CONSUMER_KEY)
		client.ClientLogin(email=data.ADMIN_EMAIL, password=data.ADMIN_PASSWORD, source='apps')
		return client