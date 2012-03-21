import gdata.apps.client
from uccal import login
from uccal import data

def getAllMembers():
	"""Lists all people in the domain
			
	"""
	
	client = gdata.apps.client.AppsClient(domain=data.CONSUMER_KEY)
	client.ClientLogin(email=data.ADMIN_EMAIL, password=data.ADMIN_PASSWORD, source='apps')
	
	client.RetrieveAllUsers()


