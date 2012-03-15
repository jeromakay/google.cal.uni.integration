#coding=utf-8
'''
Created on 12 M�rta 2012
'''
import unittest
import sqlite3
from Database import Methods
class Test(unittest.TestCase):


    def makeTable(self,conn):        
        c=conn.cursor()
        print("Creating the groups table")
        c.execute("""create table groups (
             group_id INTEGER PRIMARY KEY,
             groups_gid char(32) not null,
             title varchar(64) not null,
             description varchar(255) default null,
             group_type_id int unsigned not null,
             mod_dt int unsigned not null
            )""")
        
        print("Creating the group types table")
        c.execute("""create table group_types (
             group_type_id INTEGER PRIMARY KEY,
             title varchar(64) not null,
             description varchar(255) default null
            )""")
        
        print("Creating the modules table")
        c.execute("""create table modules (
             module_id INTEGER PRIMARY KEY,
             google_cal_id varchar(64) not null,
             title varchar(64) not null,
             description varchar(255) default null,
             mod_dt int unsigned not null
            );""")
        
        print("Creating the timetables table")
        c.execute("""create table timetables (
             module_id int unsigned not null,
             group_id int unsigned not null,
             mod_dt int unsigned not null,
             primary key ( module_id, group_id )
            );""")
        
        print("creating the users table")
        c.execute("""create table users (
             gID bigint unsigned not null,
             UID bigint unsigned not null,
             name varchar(97) not null,
             mod_dt int unsigned not null,
             primary key (gID)
            );""")
        
        print("Creating the grouped users table")
        c.execute("""create table grouped_users(
             gID bigint unsigned not null,
             group_id int unsigned not null,
             mod_dt int unsigned not null,
             primary key (gID,group_id)
            );""")
        
        print("Adding a trigger for removing grouped user data after a group is deleted")
        c.execute("""CREATE TRIGGER [delete_grouped_users]
            BEFORE DELETE
            ON [groups]
            FOR EACH ROW
            BEGIN
            DELETE FROM grouped_users WHERE grouped_users.group_id = old.group_id;
            END;""")
        
        print("Committing all tables to memory")
        conn.commit()
       
        
        return conn
    
    def testEverything(self):
        
        conn = sqlite3.connect('database.litedb')
        c=conn.cursor()
        print("checking if tables already exist")
        c.execute("select * from sqlite_master")
        if len(c.fetchall())<=0:
            conn = self.makeTable(conn)
        print("Creating 2 groups")
        Methods.CreateGroup(conn,1, "CS1101-A", "Intro to Being a DataBase, lab 1",  1)
        Methods.CreateGroup(conn,2, "CS1101-B", "Intro to Being a DataBase, lab 2", 1)
        
        print("Making a module for the 2 groups to parent")
        Methods.CreateModule(conn, 1, "CS1101", "Intro to Being a DataBase")
        
        print("Making 3 students to take the module")
        Methods.CreateUser(conn, 11, 1, "Tom Jones")
        Methods.CreateUser(conn, 12, 2, "John Doe")
        Methods.CreateUser(conn, 13, 3, "Some Guy")
        
        print("Making the 2 groups part of the module")
        Methods.AddModToGroup(conn, 1, 1)
        Methods.AddModToGroup(conn, 2, 1)
        
        print("Adding 2 users to one group, 1 user to the other")
        Methods.AddUserToGroup(conn, 1, 11)
        Methods.AddUserToGroup(conn, 1, 12)
        Methods.AddUserToGroup(conn, 2, 13)
        print("Dumping the list of students:")
        print(Methods.ListUsers(conn))
        
        print("Dumping the groups")
        print(Methods.ListGroups(conn))
        
        print("Dumping the modules")
        print(Methods.ListModules(conn))
        
        print("dumping the students in group 1")
        print(Methods.ListGroupedUsers(conn,1))
        
        print("dumping the groups in the module")
        print(Methods.ListModuleGroups(conn,1))
        
        print("Dumping the groups the third guy is in")
        print(Methods.ListUsersGroups(conn,13))
        
        print("Changing the module's title to 'cs1102'")
        Methods.EditModule(conn, 1, title='CS1102')
        
        print("Listing the modules to see if it worked")
        print(Methods.ListModules(conn))
        
        print("Changing the groups' titles to 'cs1102' to match")
        Methods.EditGroup(conn, 1, title='CS1102-A')
        Methods.EditGroup(conn, 2, title='CS1102-B')
        
        print("Listing the groups to see if it worked")
        print(Methods.ListGroups(conn))
        
        print("Swtiching them back")
        Methods.EditModule(conn, 1, title='CS1101')
        Methods.EditGroup(conn, 1, title='CS1101-A')
        Methods.EditGroup(conn, 2, title='CS1101-B')
        
        print("Verification of it working")
        print(Methods.ListModules(conn))
        print(Methods.ListGroups(conn))
        
        print("Woops, some guy dropped out")
        Methods.RemoveUserFromGroup(conn,13,2)
        Methods.DeleteUser(conn,13)
        print("This makes the second group empty and redundant")
        Methods.RemoveModFromGroup(conn,1,2)
        Methods.DeleteGroup(conn,2)
        
        print("As a result, here are the groups and students")
        print(Methods.ListGroups(conn))
        print(Methods.ListUsers(conn))
        
        print("The uni has stopped offering cs1101, and as a result its only 2 students left have dropped out")
        Methods.DeleteModule(conn,1)
        Methods.RemoveModFromGroup(conn,1,1)
        Methods.RemoveUserFromGroup(conn,11,1)
        Methods.RemoveUserFromGroup(conn,12,1)
        Methods.DeleteUser(conn,11)
        Methods.DeleteUser(conn,12)
        Methods.DeleteGroup(conn,1)
        
        print("Here is the resulting modules, groups and users; if you can see anything it's bad")
        Methods.ListModules(conn)
        Methods.ListGroups(conn)
        Methods.ListUsers(conn)
        
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.Creation']
    unittest.main()