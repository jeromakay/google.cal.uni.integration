#!/usr/bin/python
#
# Copyright (C) 2009 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import gdata.apps.groups.client
import data

def createGroup (group_id, group_name, description='no description given', email_permission=None):
	"""Creates a Google Group

		Args:
			group_id: A unique ID to refer to the group
			group_name: A name for the group
			description: describes the group
			email_permission: Email settings for the group. 
		"""

	#---login details to use---
	#user id eg abc1
	user = data.ADMIN_ID
	#user email eg abc1@example.com
	user_full = data.ADMIN_EMAIL
	#user password
	password = data.ADMIN_PASSWORD
	#the domain key eg. example.com
	CONSUMER_KEY = data.CONSUMER_KEY

	#create client object
	groupClient = gdata.apps.groups.client.GroupsProvisioningClient(domain=CONSUMER_KEY) 
	#authorize client
	groupClient.ClientLogin(email=user_full, password=password, source ='apps')
	print groupClient

	try :
		#create the group and add it to the domain
		groupClient.CreateGroup(group_id, group_name, description, email_permission)
		print "Success!"
		print group_name + " was added to " + CONSUMER_KEY + " with the ID " + group_id 
	except Exception :
		print "there was an error with your submission. \nMaybe a group with that ID already Exists?"
		
#---method to delete a group---
def deleteGroup():
	#---group details---
	group_id = 'twj_ucc_test_group'

	#---login details to use---
	#user id eg abc1
	user = data.ADMIN_ID
	#user email eg abc1@example.com
	user_full = data.ADMIN_EMAIL
	#user password
	password = data.ADMIN_PASSWORD
	#the domain key eg. example.com
	CONSUMER_KEY = data.CONSUMER_KEY

	#create client object
	groupClient = gdata.apps.groups.client.GroupsProvisioningClient(domain=CONSUMER_KEY) 
	#authorize client
	groupClient.ClientLogin(email=user_full, password=password, source ='apps')

	try :
		#delete the group
		groupClient.DeleteGroup(group_id)
		print "Success!"
		print group_id + "was deleted"
	except Exception :
		print "there was an error with your submission. \nMaybe the group does not exist?"
		
#---method to update a group---
def updateGroup():
	#---group details---
	group_id = 'twj_ucc_test_group'
	group_name = 'UPDATED Test_group'
	description = 'aN UPDATED test group to add'
	#dont know how this works yet
	#email_permission = 'None'

	#---login details to use---
	#user id eg abc1
	user = data.ADMIN_ID
	#user email eg abc1@example.com
	user_full = data.ADMIN_EMAIL
	#user password
	password = data.ADMIN_PASSWORD
	#the domain key eg. example.com
	CONSUMER_KEY = data.CONSUMER_KEY

	#create client object
	groupClient = gdata.apps.groups.client.GroupsProvisioningClient(domain=CONSUMER_KEY) 
	#authorize client
	groupClient.ClientLogin(email=user_full, password=password, source ='apps')
	
	newGroupDetail = gdata.apps.groups.data.GroupEntry(group_id, group_name, description)
	
	try :
		#change the group details
		groupClient.UpdateGroup(group_id, newGroupDetail)#, description, email_permission)
		print "Success!"
		print group_id + " was updated" 
	except Exception :
		print "there was an error with your submission. \nMaybe the group does not exist?"
		
#---method to add a membet to a group
def addGroupMember ():
	#---user and group details---
	group_id = 'twj_ucc_test_group'
	member_id = 'twj2'

	#---login details to use---
	#user id eg abc1
	user = data.ADMIN_ID
	#user email eg abc1@example.com
	user_full = data.ADMIN_EMAIL
	#user password
	password = data.ADMIN_PASSWORD
	#the domain key eg. example.com
	CONSUMER_KEY = data.CONSUMER_KEY

	#create client object
	groupClient = gdata.apps.groups.client.GroupsProvisioningClient(domain=CONSUMER_KEY) 
	#authorize client
	groupClient.ClientLogin(email=user_full, password=password, source ='apps')

	try :
		#add user to the group
		groupClient.AddMemberToGroup(group_id, member_id)
		print "Success!"
		print member_id + " was added to " + group_id 
	except Exception :
		print "there was an error with your submission. \nMaybe the user is already a member?"
		
#---method to delete a member from a group---
def deleteGroupMember ():
	#---user and group details---
	group_id = 'twj_ucc_test_group'
	member_id = 'twj2'

	#---login details to use---
	#user id eg abc1
	user = data.ADMIN_ID
	#user email eg abc1@example.com
	user_full = data.ADMIN_EMAIL
	#user password
	password = data.ADMIN_PASSWORD
	#the domain key eg. example.com
	CONSUMER_KEY = data.CONSUMER_KEY

	#create client object
	groupClient = gdata.apps.groups.client.GroupsProvisioningClient(domain=CONSUMER_KEY) 
	#authorize client
	groupClient.ClientLogin(email=user_full, password=password, source ='apps')

	try :
		#delete user from group
		groupClient.RemoveMemberFromGroup(group_id, member_id)
		print "Success!"
		print member_id + " was removed from " + group_id 
	except Exception :
		print "there was an error with your submission. \nMaybe the user is not a member?"