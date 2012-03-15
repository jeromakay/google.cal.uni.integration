#coding=utf-8
'''
Created on 12 M�rta 2012
'''
import unittest
import sqlite3
from Database import DB
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
        DB.CreateGroup(conn,1, "CS1101-A", "Intro to Being a DataBase, lab 1",  1)
        DB.CreateGroup(conn,2, "CS1101-B", "Intro to Being a DataBase, lab 2", 1)
        
        print("Making a module for the 2 groups to parent")
        DB.CreateModule(conn, 1, "CS1101", "Intro to Being a DataBase")
        
        print("Making 3 students to take the module")
        DB.CreateUser(conn, 11, 1, "Tom Jones")
        DB.CreateUser(conn, 12, 2, "John Doe")
        DB.CreateUser(conn, 13, 3, "Some Guy")
        
        print("Making the 2 groups part of the module")
        DB.AddModToGroup(conn, 1, 1)
        DB.AddModToGroup(conn, 2, 1)
        
        print("Adding 2 users to one group, 1 user to the other")
        DB.AddUserToGroup(conn, 1, 11)
        DB.AddUserToGroup(conn, 1, 12)
        DB.AddUserToGroup(conn, 2, 13)
        print("Dumping the list of students:")
        print(DB.ListUsers(conn))
        
        print("Dumping the groups")
        print(DB.ListGroups(conn))
        
        print("Dumping the modules")
        print(DB.ListModules(conn))
        
        print("dumping the students in group 1")
        print(DB.ListGroupedUsers(conn,1))
        
        print("dumping the groups in the module")
        print(DB.ListModuleGroups(conn,1))
        
        print("Dumping the groups the third guy is in")
        print(DB.ListUsersGroups(conn,13))
        
        print("Changing the module's title to 'cs1102'")
        DB.EditModule(conn, 1, title='CS1102')
        
        print("Listing the modules to see if it worked")
        print(DB.ListModules(conn))
        
        print("Changing the groups' titles to 'cs1102' to match")
        DB.EditGroup(conn, 1, title='CS1102-A')
        DB.EditGroup(conn, 2, title='CS1102-B')
        
        print("Listing the groups to see if it worked")
        print(DB.ListGroups(conn))
        
        print("Swtiching them back")
        DB.EditModule(conn, 1, title='CS1101')
        DB.EditGroup(conn, 1, title='CS1101-A')
        DB.EditGroup(conn, 2, title='CS1101-B')
        
        print("Verification of it working")
        print(DB.ListModules(conn))
        print(DB.ListGroups(conn))
        
        print("Woops, some guy dropped out")
        DB.RemoveUserFromGroup(conn,13,2)
        DB.DeleteUser(conn,13)
        print("This makes the second group empty and redundant")
        DB.RemoveModFromGroup(conn,1,2)
        DB.DeleteGroup(conn,2)
        
        print("As a result, here are the groups and students")
        print(DB.ListGroups(conn))
        print(DB.ListUsers(conn))
        
        print("The uni has stopped offering cs1101, and as a result its only 2 students left have dropped out")
        DB.DeleteModule(conn,1)
        DB.DeleteUser(conn,11)
        DB.DeleteUser(conn,12)
        DB.DeleteGroup(conn,1)
        
        print("Here is the resulting modules, groups and users; if you can see anything it's bad")
        DB.ListModules(conn)
        DB.ListGroups(conn)
        DB.ListUsers(conn)
        
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.Creation']
    unittest.main()