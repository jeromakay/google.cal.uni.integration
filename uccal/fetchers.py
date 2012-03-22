from Database import DB

def fetch( dataType, subDataID=None ):
	if dataType == "groups":
		return DB.ListGroups()
	if dataType == "modules":
		return DB.ListModules()
	return json