'''
Created on 12 Márta 2012

@author: home
'''
import json
import sqlite3 as sqlite
#DELETES THE GROUP SPECIFIED BY Group_id, RETURNS 1 IF SUCCESSFUL, 0 Otherwise
def DeleteGroup(database,
                 group_id
                 ):
    
    connect=sqlite.connect(database)
    c=connect.cursor
    #finds the group identifier, precedence given to id
    
    c.execute("""DELETE FROM groups AS old
                        WHERE group_id=?""",group_id)
    
    connect.commit()
    c.close()
       
    return 1

