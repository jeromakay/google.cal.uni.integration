def Delete(dataType, EntityID):
	if dataType == "group":
		from uccal import Groups
		Groups.deleteGroup(EntityID)
	if dataType == "module":
		from uccal import Modules
		Modules.deleteModule(EntityID)