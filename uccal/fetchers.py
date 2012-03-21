from Database import DB

def fetch():
	json = DB.TestListGroups()
	return json