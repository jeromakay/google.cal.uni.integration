'''
Created on 12 Márta 2012

@author: home
'''
import json
import sqlite3 as sqlite
#RETURNS A JSON STRING REPRESENTING ALL USERS IN A SPECIFIED GROUP
def ListGroupedUsers(database,group_id):
    
    connect=sqlite.connect(database)
    c=connect.cursor
    
    c.execute("""SELECT users.gID,users.name
                FROM grouped_users,users
                WHERE group_id=?
                    AND users.gID=grouped_users.gID""",group_id)
    
    json_return=[]
    i=0
    for row in c:
        json_return[i]={"gID":row[0],
                        "name":row[1]}
        ++i
      
    c.close()
    json.dumps(json_return)
        
    return json_return

