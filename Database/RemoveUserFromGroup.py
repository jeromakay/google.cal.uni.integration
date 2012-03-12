'''
Created on 12 Márta 2012

@author: home
'''
import json
import sqlite3 as sqlite
#DELETES THE GROUP SPECIFIED BY Group_id OR Group_Name, RETURNS 1 IF SUCCESSFUL, 0 Otherwise
def RemoveUserFromGroup(database,
                 user_id,
                 group_id
                 ):
    
    connect=sqlite.connect(database)
    c=connect.cursor
    #finds the group identifier, precedence given to id
    c.execute("""DELETE FROM grouped_users
                        WHERE gID=?""",user_id)
    
    connect.commit()
    c.close

