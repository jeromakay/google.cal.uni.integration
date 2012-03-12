'''
Created on 12 Márta 2012

@author: home
'''
import json
import sqlite3 as sqlite
#DELETES THE GROUP SPECIFIED BY Group_id OR Group_Name, RETURNS 1 IF SUCCESSFUL, 0 Otherwise
def EditModule(database,
                 module_id,
                 title=None,
                 description=None,
                 group_type=None
                 ):
    
    connect=sqlite.connect(database)
    c=connect.cursor
    #finds the group to be modified
    c.execute("""SELECT title,description
                FROM modules
                WHERE module_id=?""",module_id)
    
    for row in c:
        if title is None:
            title=row[0]
        if description is None:
            description=row[1]
       
    
    c.execute("""UPDATE modules
                SET title=?,description=?
                WHERE module_id=?""",title,description,group_type)
    
    connect.commit()
    c.close()
       
    return 1
