'''
Created on 12 Márta 2012

@author: home
'''
import sqlite3 as sqlite
#CREATES A GROUP, NAMED <group_Name, 'New_group' by default>, OF TYPE <type_id,
# default whatever 0 is> WITH DESCRIPTION <description, 'Generic_group'by
# default
def CreateModule(database,
                 cal_id,
                 title="New_Module",
                 desc="Generic_Module"
                 ):
    
    connect=sqlite.connect(database)
    
    #creates the module in the database
    c=connect.cursor
    c.execute("""insert into modules(title,description,)
          values (?,?)""",title,desc)
    
    connect.commit()
    c.close



