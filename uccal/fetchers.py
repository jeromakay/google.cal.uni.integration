from Database import DB

def fetch( dataType, subDataID=None ):
	if dataType == "groups":
		return DB.ListGroups()
	if dataType == "modules":
		return DB.ListModules()
	if dataType == "users":
		if subDataID != None:
			return DB.ListGroupedUsers(subDataID)
		else:
			return DB.ListUsers()