#coding=utf-8

'''
Created on 12 M�rta 2012

@author: home
'''
import simplejson as json
import datetime
from Datastores import  Module,User,Group,GroupType
from google.appengine.ext import db


#import google.appengine.api.datastore.Entity;
#import google.appengine.api.datastore.Query;

def CreateGroupType(name, desc):
    
        """Creates a group
        inputs:
        --gid - the google ID of the group
        --group_name - the name of the group
        --description - a brief summary of the new group
        type_id - the type of group it is
        """
        e = GroupType(title=name,
                  description=desc)
        e.mod_dt = datetime.datetime.now()
        
        
        if GroupType.gql("ORDER BY group_type_id DESC").count()<=0:
            e.group_type_id=0
        else:
            max_group_type=GroupType.gql("ORDER BY group_type_id DESC").get()
            e.group_type_id=max_group_type.group_type_id+1        
        e.put()
        while not(e.is_saved()):
            None
        return e.group_type_id


def CreateGroup(gid,
                 group_Name,
                 desc,
                 type_id):
    
        """Creates a group
        inputs:
        --gid - the google ID of the group
        --group_name - the name of the group
        --description - a brief summary of the new group
        type_id - the type of group it is
        """
        e = Group(group_gid=gid,
                  title=group_Name,
                  description=desc)
        e.mod_dt = datetime.datetime.now()
        
        
        if Group.gql("ORDER BY group_id DESC").count()<=0:
            e.group_id=0
        else:
            max_group=Group.gql("ORDER BY group_id DESC").get()
            e.group_id=max_group.group_id+1
        
        e.group_type=GroupType.gql("WHERE group_type_id=:1",type_id).get()
        
        e.put()
        while not(e.is_saved()):
            None
        return e.group_id

def AddModToGroup(
                 group_id,
                 module_id):
        """Adds a specified module to a group (or vice-versa)
        inputs:
        --Group_id - the group's identifier
        --module_id - the module's identifier
        """
        
        
        e=Group.gql("WHERE title=:1",group_id).get()
        f=Module.gql("WHERE title=:1",module_id).get()
        
        if f.key() not in e.group_modules:
            e.group_modules.append(f.key())
            e.put()
        

def AddUserToGroup(
                 group_id,
                 user_id):
        """Adds a specified user to a group
        inputs:
        --Group_id - the group's identifier
        --user_id - the user's google account identifier
        """
        
        e=Group.gql("WHERE group_id=:1",group_id).get()
        f=User.gql("WHERE user_id=:1",user_id).get()
        
        if e.key() not in f.user_groups:
            f.user_groups.append(e.key())
            f.put()
        
        
def CreateModule(cal_id,
                 name,
                 desc):
        """Creates a module
        inputs:
        --title - the name of the module; "Default Module" by default
        --desc - a brief summary of the new module; "Generic_module" by default
        --cal_id - the ID of the calendar associated with the module
        """
        
        
        #creates the module in the database
        e=Module(title=name,
                 description=desc,
                 google_cal_id=cal_id)
        e.mod_dt=datetime.datetime.now()
        
        if Module.gql("ORDER BY module_id DESC").count()<=0:
            e.module_id=0
        else:
            max_mod=Module.gql("ORDER BY module_id DESC").get()
            e.module_id=max_mod.module_id+1
        
        
        e.put()
        while not(e.is_saved()):
            None
        return e.module_id

def CreateUser(  gid,
                 uid,
                 name):
    
        """Creates a user
        inputs:
        --gid - the Google ID of the user
        --uid - the Uni ID of the user
        --name - the user's name
        """
        e=User(gID=gid,uID=uid,name=name)
        e.mod_dt=datetime.datetime.now()
        
        if User.gql("ORDER BY user_id DESC").count()<=0:
            e.user_id=0
        else:
            max_user=User.gql("ORDER BY user_id DESC").get()
            e.user_id=max_user.user_id+1
        
        e.put()
        while not(e.is_saved()):
            None
        return e.user_id

def DeleteGroup(group_id
                 ):
        """Deletes a group
        inputs:
        --group_id - the ID of the group to delete
        """
        e=Group.gql("WHERE group_id=:1",group_id).get()
        db.delete(e)
        while e.is_saved():
            None
       
       
def DeleteModule(module_id
                 ):
        """Deletes a module
        inputs:
        --group_id - the ID of the module to delete
        """
        e=Module.gql("WHERE module_id=:1",module_id).get()
        db.delete(e)
        


def DeleteUser(user_id
                 ):
    
        """Deletes a user
        inputs:
        --group_id - the ID of the user to delete
        """
        
        e=User.gql("WHERE user_id=:1",user_id).get()
        db.delete(e)
        while e.is_saved():
            None


def EditGroup(group_id,
              newName=None,
              newDesc=None,
              newType=None
                 ):
    
        """Edits a group specified by the ID
        inputs:
        --group_id - the ID of the group to edit
        --title - if changed, the new title of the group
        --description - if changed, the new description of the group
        --group_type - if changed, the new type of the group
        """
        e=Group.gql("WHERE group_id=:1",group_id).get()
        if newName is not None:
            e.title=newName
        if newDesc is not None:
            e.description=newDesc
        if newType is not None:
            e.group_type=GroupType.gql("WHERE title=:1",newType).get()      
        e.mod_dt=datetime.datetime.now()
        
        e.put()
        

def EditModule(mod_id,
               newName=None,
               newDesc=None,
               newCal=None
                 ):
        """Edits a module specified by the ID
        inputs:
        --module_id - the ID of the module to edit
        --title - if changed, the new title of the module
        --description - if changed, the new description of the module
        """
        e=Module.gql("WHERE module_id=:1",mod_id).get()
        if newName is not None:
            e.title=newName
        if newDesc is not None:
            e.description=newDesc
        if newCal is not None:
            e.google_cal_id=newCal     
        e.mod_dt=datetime.datetime.now()
        
        e.put()

def ListGroupedUsers(group_id):
        """Lists the users in a group
        inputs:
        --group_id - the ID of the group to show    
        """
       
        the_group=Group.gql("WHERE group_id=:1",group_id ).get()
        Users=the_group.users()
        json_return=[]
        for person in Users:
            if the_group in person.users_groups:
                json_return.append({"name":person.name,
                                    "id":person.user_id,
                                    "gid":person.gID,
                                    "uid":person.uID})
        return json.dumps(json_return)
            

def ListGroups():
        """Lists the groups on file
        """
       
        json_return = []
        Groups=Group.gql("")    
        for group in Groups:
            json_return.append({"name":group.title,
                                "id":group.group_id,
                                "desc":group.description,
                                "gid":group.group_gid,
                                "type":group.group_type})
        return json.dumps(json_return)
            
    
def ListGroupTypes():
        """Lists the types of groups on file
        """
        json_return = []
        GroupTypes=GroupType.gql("")    
        for grouptype in GroupTypes:
            json_return.append({"name":grouptype.title,
                                "id":grouptype.group_type_id,
                                "desc":grouptype.description})
        return json.dumps(json_return)
            
    
def ListModuleGroups(module_id):
        """Lists the groups attatched to a module
        inputs:
        --module_id - the ID of the module to show    
        """
        the_module=Module.gql("WHERE module_id=:1",module_id ).get()
        Groups=the_module.groups()
        json_return=[]
        for group in Groups:
                json_return.append({"name":group.title,
                                    "id":group.group_id,
                                "desc":group.description,
                                "gid":group.group_gid,
                                "type":group.group_type})
        return json.dumps(json_return)
        
    
def ListModules():
        """Lists the modules on file
        """
        
        json_return = []
        Modules=Module.gql("")    
        for module in Modules:
            json_return.append({"name":module.title,
                                "id":module.module_id,
                                "desc":module.description,
                                "cal_id":module.google_cal_id})
        return json.dumps(json_return)
            
       

    
def ListUsers():
        """Lists the users on file
        """
        Users=User.gql("")
        json_return=[]
        for user in Users:
            json_return.append({"name":user.name,
                                "id":user.user_id,
                                "gid":user.gID,
                                "uid":user.uID})
        return json.dumps(json_return)
    
def ListUsersGroups(user_id):
        """Lists the groups a user is in
        inputs:
        --user_id - the ID of the user to show    
        """
        user=User.gql("WHERE user_id=:1",user_id).get()
        json_return=[]
        for group in user.users_groups:
            json_return.append({"name":group.title,
                                "id":group.group_id,
                                "desc":group.description,
                                "gid":group.group_gid,
                                "type":group.group_type})
        return json.dumps(json_return)
            

def ListUsersModules(user_id):
        """Lists the modules a user is taking
        inputs:
        --user_id - the ID of the user to show    
        """
        the_user=User.gql("WHERE user_id=:1",user_id).get()
        groups=[]
        for user_group in the_user.users_groups:
            groups.append(Group.gql("WHERE key=:1",user_group))
        modules=[]
        for group in groups:
            for module in group.group_modules:
                if module not in modules:
                    modules.append(module)
        
        json_return=[]
        for module in modules:
            json_return.append({"name":module.title,
                                "id":module.module_id,
                                "desc":module.description,
                                "cal_id":module.google_cal_id})
        return json.dumps(json_return)
            
    
def RemoveModFromGroup(module_id,
                 group_id
                 ):
        """Deletes a module from a group
        inputs:
        --group_id - the ID of the group to modify
        --module_id - the ID of the module to sever
        """
        
        e=Group.gql("WHERE title=:1",group_id).get()
        f=Module.gql("WHERE title=:1",module_id).get()
        
        if f.key() in e.group_modules:
            e.group_modules.remove(f.key())
            e.put()
        
def RemoveUserFromGroup(
                 user_id,
                 group_id
                 ):
        """Removes a user from the group
        inputs:
        --user_id - the google ID of the user to remove
        --group_id - the ID of the affected group
        """
        
        e=Group.gql("WHERE title=:1",group_id).get()
        f=User.gql("WHERE title=:1",user_id).get()
        
        if e.key() in f.user_groups:
            f.user_groups.remove(e.key())
            f.put()

def TestListGroups():
##
    json_encode= {'results': [ 
                                {'id': 1, 'group_type': 1, 'group_gid': '2dabd109cf892b94e72563da710669c4', 'title': 'LOLOLOLOL', 'description': 'Everyone in Web Systems Engineering'}, 
                                {'id': 2, 'group_type': 1, 'group_gid': 'ee8efdd53326e275390b866473aac247', 'title': 'food_and_science_ck401_3rd_cs', 'description': 'Everyone in Computer Science Hons'},
                                {'id': 3, 'group_type': 1, 'group_gid': '9f1319fde74c8ca728ec7452d4e85521', 'title': 'arts_music', 'description': 'Everyone studying Music Hons.'}, 
                                {'id': 4, 'group_type': 2, 'group_gid': '9459e2b377f25454ee47133c03205076', 'title': 'arts_music_trad_music_lecturers', 'description': 'Lecturers teaching Trad Irish Music.'}, 
                                {'id': 5, 'group_type': 3, 'group_gid': '7e9cf516ec7fcc55476fe44696cfca66', 'title': 'foot_and_science_microbiology_lab_assist', 'description': 'Labs assistants for the microbiology lectures labs.'},
                               {'id': 7, 'group_type': 1, 'group_gid': 'wse@jeromakay.com', 'title': 'real_deal', 'description': 'This is the real deal.'} ],
                                
                            'groupTypes': [
                                {'id': 1, 'name': 'students'},
                                {'id': 2, 'name': 'lecturers'},
                                {'id': 3, 'name': 'assistants'}
                            ] }
    
    return json.dumps(json_encode)
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        