'''
Created on 12 Márta 2012

@author: home
'''
import sqlite3 as sqlite
#CREATES A GROUP, NAMED <group_Name, 'New_group' by default>, OF TYPE <type_id,
# default whatever 0 is> WITH DESCRIPTION <description, 'Generic_group'by
# default
def AddModToGroup(database,
                 group_id,
                 module_id):
    
    connect=sqlite.connect(database)
    
    #creates the group in the database
    c=connect.cursor
    c.execute("""insert into timetables(group_id,module_id)
          values (?,?)""",group_id,module_id)
    
    connect.commit() 
     
    c.close()
    
