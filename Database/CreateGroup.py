'''
Created on 12 Márta 2012

@author: home
'''
import json
import sqlite3 as sqlite
#CREATES A GROUP, NAMED <group_Name, 'New_group' by default>, OF TYPE <type_id,
# default whatever 0 is> WITH DESCRIPTION <description, 'Generic_group'by
# default
def CreateGroup(database,
                 group_Name,
                 description,
                 gid,
                 type_id):
    
    connect=sqlite.connect(database)
    
    #creates the group in the database
    c=connect.cursor
    c.execute("""insert into groups(title,groups_gid,description,group_type_id)
          values (?,?,?,?)""",group_Name,gid,description,type_id)
    
    connect.commit() 
     
    #finds the id to output
    c.execute("""SELECT MAX group_id
                FROM groups""")    
    group_id = c.fetchone()[0]   
    c.close()
    return group_id

