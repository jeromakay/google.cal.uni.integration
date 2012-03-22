import gdata.apps.groups.client
import data
	
def adminLogin(type=None, user_id=None):
	
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
	
	if type == "2legstudent":
		requestor_id = user_id + '@' + data.CONSUMER_KEY
		two_legged_oauth_token = gdata.gauth.TwoLeggedOAuthHmacToken(
			data.CONSUMER_KEY, data.CONSUMER_SECRET, requestor_id)

		client = gdata.calendar.client.CalendarClient(source=data.SOURCE_APP_NAME)
		client.auth_token = two_legged_oauth_token
		return client