def Delete(dataType, EntityID):
	if dataType == "group":
		from groups import delete
		delete.deleteGroup(EntityID)