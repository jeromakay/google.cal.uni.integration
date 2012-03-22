import gdata.apps.groups.client

import random
import hashlib

from uccal import login
from uccal import data
from Database import DB

def createGroup (group_name, description='no description given', type_id=0, email_permission=None):
	"""Creates a Google Group with the given paramaters 

		Args:
			group_name: A name for the group
			description: describes the group
			type_id: The type of members of the group (eg student, staff) represented by an int (see database documentation)
			email_permission: Email settings for the group. 
	"""

	#generate hashed id
	group_id = hashlib.md5(group_name).hexdigest()
	
	#deal with database here
	DB.CreateGroup(group_id, group_name, description, type_id)
	
	#create client object
	groupClient = login.adminLogin()

	#create the group and add it to the domain
	groupClient.CreateGroup(group_id, group_name, description, email_permission)
		
#---method to delete a group---
def deleteGroup(group_id):
	"""Deletes the google groups with the given ID

		Args:
			group_id: A name for the group
			
	"""
	#deal with database here
	DB.DeleteGroup(group_id)
	
	#create client object
	groupClient = login.adminLogin()
	
	#delete the group
	groupClient.DeleteGroup(group_id)

def updateGroup(group_id, new_group_name, new_description='no description given', new_type_id=1, new_email_permission=None):
	"""Updates a google group with the given paramaters 
	
		Args:
			group_id: the ID of the group to update
			group_name: A new name for the group
			description: A new description for the group
			type_id: The type of members of the group (eg student, staff) represented by an int (see database documentation)
			email_permission: Email settings for the group.
	"""

	#create client object
	groupClient = login.adminLogin()
		
	#deal with database here
	DB.EditGroup(group_id, new_group_name, new_description, new_group_type)
	
	#change the group details
	groupClient.UpdateGroup(group_id, new_group_name, new_description, email_permission)


#---method to add a member to a group
def addGroupMember (group_id, member_id):
	"""Adds the members to the group
	
		Args:
			group_id: the ID of the group to update
			members_array: the users to add
			
	"""
	
	#deal with database here
	DB.AddUserToGroup(group_id, member_id)
	
	#create client object
	groupClient = login.adminLogin()
	
	#add users to the group
	groupClient.AddMemberToGroup(group_id, member_id)
		
#---method to delete a member from a group---
def deleteGroupMember (group_id, members_array):
	"""Deletes the members from a group
	
		Args:
			group_id: the ID of the group to update
			members_array: the users to add
			
	"""
	
	#deal with database here
	DB.EditGroup(group_id, new_group_name, new_description, new_group_type)
	
	#create client object
	groupClient = login.adminLogin()
	
	#delete users to the group
	for member_id in members_array:
		groupClient.RemoveMemberFromGroup(group_id, member_id)