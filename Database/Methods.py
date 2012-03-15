#coding=utf-8

'''
Created on 12 M�rta 2012

@author: home
'''
import json
import time
def CreateGroup(connect, gid,
                 group_Name="Default Group",
                 description="A normal group",
                
                 type_id=0):
    
        """Creates a group
        inputs:
        --group_name - the name of the group; "Default Group" by default
        --description - a brief summary of the new group; "A normal group" by default
        --gid - the google ID of the group
        type_id - the type of group it is; 0 by default
        """
        
        
        #creates the group in the database
        c=connect.cursor()
        t=(group_Name,gid,description,type_id,getDate())
        c.execute("""insert into groups(title,groups_gid,description,group_type_id,mod_dt)
              values (?,?,?,?,?)""",t)
        
        connect.commit() 
         
        #finds the id to output
        c.close()

def AddModToGroup(connect,
                 group_id,
                 module_id):
        """Adds a specified module to a group (or vice-versa)
        inputs:
        --Group_id - the group's identifier
        --module_id - the module's identifier
        """
        
        
        #creates the group in the database
        c=connect.cursor()
        t=(group_id,module_id,getDate())
        c.execute("""insert into timetables(group_id,module_id,mod_dt)
              values (?,?,?)""",t)
        
        connect.commit() 
         
        c.close()
        
def AddUserToGroup(connect,
                 group_id,
                 user_id):
        """Adds a specified user to a group
        inputs:
        --Group_id - the group's identifier
        --user_id - the user's google account identifier
        """
        
        #creates the group in the database
        c=connect.cursor()
        t=(group_id,user_id,getDate())
        c.execute("""insert into grouped_users(group_id,gID,mod_dt)
              values (?,?,?)""",t)
        
        connect.commit() 
         
        c.close()
        
        
def CreateModule(connect,
                 cal_id,
                 title="New_Module",
                 desc="Generic_Module"
                 ):
        """Creates a module
        inputs:
        --title - the name of the module; "Default Module" by default
        --desc - a brief summary of the new module; "Generic_module" by default
        --cal_id - the ID of the calendar associated with the module
        """
        
        
        #creates the module in the database
        c=connect.cursor()
        t=(cal_id,title,desc,getDate())
        c.execute("""insert into modules(google_cal_id,title,description,mod_dt)
              values (?,?,?,?)""",t)
        
        connect.commit()
        c.close

def CreateUser(connect,
                 gid,
                 uid,
                 name):
    
        """Creates a user
        inputs:
        --gid - the Google ID of the user
        --uid - the Uni ID of the user
        --name - the user's name
        """
        
        
        #creates the group in the database
        c=connect.cursor()
        t=(gid,uid,name,getDate())
        c.execute("""insert into users(gID,UID,name,mod_dt)
              values (?,?,?,?)""",t)
        
        connect.commit() 
         
        #finds the id to output
        c.close()

def DeleteGroup(connect,
                 group_id
                 ):
        """Deletes a group
        inputs:
        --group_id - the ID of the group to delete
        """
        
        c=connect.cursor()
        t=group_id,
        c.execute("""DELETE FROM timetables
                            WHERE group_id=?""",t)
        c.execute("""DELETE FROM grouped_users
                            WHERE group_id=?""",t)
        c.execute("""DELETE FROM groups
                            WHERE group_id=?""",t)
        
        connect.commit()
        c.close()
       
def DeleteModule(connect,
                 module_id
                 ):
        """Deletes a module
        inputs:
        --group_id - the ID of the module to delete
        """
        
        c=connect.cursor()
        #finds the group identifier, precedence given to id
        t=module_id,
        c.execute("""DELETE FROM timetables
                            WHERE module_id=?""",t)
        c.execute("""DELETE FROM modules
                            WHERE module_id=?""",t)
        
        connect.commit()
        c.close()


def DeleteUser(connect,
                 user_id
                 ):
    
        """Deletes a user
        inputs:
        --group_id - the ID of the user to delete
        """
        
        c=connect.cursor()
        t=user_id,
        #finds the group identifier, precedence given to id
        c.execute("""DELETE FROM grouped_users
                            WHERE gID=?""",t)
        c.execute("""DELETE FROM users
                            WHERE gID=?""",t)
        
        connect.commit()
        c.close


def EditGroup(connect,
                 group_id,
                 title=None,
                 description=None,
                 group_type=None
                 ):
    
        """Edits a group specified by the ID
        inputs:
        --group_id - the ID of the group to edit
        --title - if changed, the new title of the group
        --description - if changed, the new description of the group
        --group_type - if changed, the new type of the group
        """
        
        c=connect.cursor()
        #finds the group to be modified
        t=group_id,
        c.execute("""SELECT title,description,group_type_id
                    FROM groups
                    WHERE group_id=?""",t)
        
        for row in c:
            if title is None:
                title=row[0]
            if description is None:
                description=row[1]
            if group_type is None:
                group_type=row[2]
        t=(title,description,group_type,getDate(),group_id)
        c.execute("""UPDATE groups
                    SET title=?,description=?,group_type_id=?,mod_dt=?
                    WHERE group_id=?""",t)
        
        connect.commit()
        c.close()

def EditModule(connect,
                 module_id,
                 title=None,
                 description=None,
                 ):
        """Edits a module specified by the ID
        inputs:
        --module_id - the ID of the module to edit
        --title - if changed, the new title of the module
        --description - if changed, the new description of the module
        """
        c=connect.cursor()
        #finds the group to be modified
        t=module_id,
        c.execute("""SELECT title,description
                    FROM modules
                    WHERE module_id=?""",t)
        
        for row in c:
            if title is None:
                title=row[0]
            if description is None:
                description=row[1]
           
        t=(title,description,getDate(),module_id)
        c.execute("""UPDATE modules
                    SET title=?,description=?,mod_dt=?
                    WHERE module_id=?""",t)
        
        connect.commit()
        c.close()

def ListGroupedUsers(connect,group_id):
        """Lists the users in a group
        inputs:
        --group_id - the ID of the group to show    
        """
        c=connect.cursor()
        t=group_id,
        c.execute("""SELECT users.gID,users.name
                    FROM grouped_users,users
                    WHERE group_id=?
                        AND users.gID=grouped_users.gID""",t)
        
        json_return=[]
        i=0
        for row in c:
            json_return.append({"gID":row[0],
                            "name":row[1]})
            ++i
          
        c.close()
        json.dumps(json_return)
            
        return json_return

def ListGroups(connect):
        """Lists the groups on file
        """
        c=connect.cursor()
        
        c.execute("""SELECT group_id, title,description,group_type_id,mod_dt,groups_gid
                    FROM groups""")
        
        json_return = []
        i=0    
        for row in c:
            json_return.append({"id": row[0],
                "title":row[1],
            "description":row[2],
            "type_id":row[3],
            "mod_dt":row[4],
            "group_gid":row[5]})
            ++i
        c.close()
    
        json.dumps(json_return)
            
        return json_return
    
def ListGroupTypes(connect):
        """Lists the types of groups on file
        """
        c=connect.cursor()
        
        c.execute("""SELECT group_type_id, title,description
                    FROM group_types""")
        
        json_return = []
        i=0    
        for row in c:
            json_return.append({"id": row[0],
                "title":row[1],
            "description":row[2]})
            ++i
        c.close()
    
        json.dumps(json_return)
            
        return json_return
    
def ListModuleGroups(connect,module_id):
        """Lists the groups attatched to a module
        inputs:
        --module_id - the ID of the module to show    
        """
        c=connect.cursor()
        t=module_id,
        c.execute("""SELECT groups.group_id, groups.title,groups.description,groups.group_type_id,groups.mod_dt,
                            groups.groups_gid
                    FROM timetables,groups
                    WHERE timetables.module_id=?
                        AND timetables.group_id=groups.group_id""",t)
        
        json_return = []
        i=0
        
        for row in c:
            json_return.append({"id": row[0],
                "title":row[1],
            "description":row[2],
            "type_id":row[3],
            "mod_dt":row[4],
            "group_gid":row[5]})
            ++i
        c.close()
    
        json.dumps(json_return)
            
        return json_return
    
def ListModules(connect):
        """Lists the modules on file
        """
        
        c=connect.cursor()
        
        c.execute("""SELECT module_id,google_cal_id,title,description,mod_dt
                    FROM modules""")
        
        json_return = []
        i=0
        
        for row in c:
            json_return.append({"id": row[0],
                "cal_id":row[1],
            "title":row[2],
            "description":row[3],
            "mod_dt":row[4]})
            ++i
        c.close
    
        json.dumps(json_return)
            
        return json_return

    
def ListUsers(connect):
        """Lists the users on file
        """
        c=connect.cursor()
        
        c.execute("""SELECT gID, UID,name,mod_dt
                    FROM users""")
        
        json_return = []
        i=0
        
        for row in c:
            json_return.append({"gID": row[0],
                "UID":row[1],
            "name":row[2],
            "mod_dt":row[3]})
            ++i
        c.close()
    
        json.dumps(json_return)
            
        return json_return
    
def ListUsersGroups(connect,user_id):
        """Lists the groups a user is in
        inputs:
        --user_id - the ID of the user to show    
        """
        c=connect.cursor()
        t=user_id,
        c.execute("""SELECT groups.group_id, groups.title,groups.description,groups.group_type_id,groups.mod_dt,
                            groups.groups_gid
                    FROM groups,grouped_users
                    WHERE groups.group_id = grouped_users.group_id
                        AND grouped_users.gID = ?""",t)
        
        json_return = []
        i=0
        
        for row in c:
            json_return.append({"id": row[0],
                "title":row[1],
            "description":row[2],
            "type_id":row[3],
            "mod_dt":row[4],
            "gid":row[5]})
            ++i
        c.close()
    
        json.dumps(json_return)
            
        return json_return

def ListUsersModules(connect,user_id):
        """Lists the modules a user is taking
        inputs:
        --user_id - the ID of the user to show    
        """
        c=connect.cursor()
        
        c.execute("""SELECT modules.module_id, modules.title,modules.description,modules.google_cal_id,modules.mod_dt
                    FROM grouped_users,timetables,modules
                    WHERE timetables.group_id = grouped_users.group_id
                        AND timetables.module_id = modules.module_id
                        AND grouped_users.gID = ?""",user_id)
        
        json_return = []
        i=0
        
        for row in c:
            json_return.append({"id": row[0],
                "title":row[1],
            "description":row[2],
            "cal_id":row[3],
            "mod_dt":row[4]})
            ++i
        c.close()
    
        json.dumps(json_return)
            
        return json_return
    
def RemoveModFromGroup(connect,
                 module_id,
                 group_id
                 ):
        """Deletes a module from a group
        inputs:
        --group_id - the ID of the group to modify
        --module_id - the ID of the module to sever
        """
        
        c=connect.cursor()
        #finds the group identifier, precedence given to id
        t=(group_id,module_id)
        c.execute("""DELETE FROM timetables
                            WHERE group_id=?
                            AND module_id=?""",t)
        
        connect.commit()
        c.close
        
def RemoveUserFromGroup(connect,
                 user_id,
                 group_id
                 ):
        """Removes a user from the group
        inputs:
        --user_id - the google ID of the user to remove
        --group_id - the ID of the affected group
        """
        
        c=connect.cursor()
        t=user_id,group_id
        #finds the group identifier, precedence given to id
        c.execute("""DELETE FROM grouped_users
                            WHERE gID=?
                            AND group_id=?""",t)
        
        connect.commit()
        c.close

def getDate():
    
    millis = int(round(time.time() * 1000))
    return millis



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        