'''
Created on 12 Márta 2012

@author: home
'''
import json
import sqlite3 as sqlite
#RETURNS A JSON STRING REPRESENTING ALL GROUPS IN THE DATABASE
def ListModuleUsers(database,module_id):
    
    connect=sqlite.connect(database)
    c=connect.cursor
    
    c.execute("""SELECT users.gID,users.name
                FROM grouped_users,timetables, users
                WHERE timetables.module_id=?
                    AND timetables.group_id = grouped_users.group_id
                    AND grouped_users.gID = users.gID""",module_id)
    
    json_return = []
    i=0
    
    for row in c:
        json_return[i] = {"gID": row[0],
                          "name":row[1]}
        ++i
    c.close()

    json.dumps(json_return)
        
    return json_return

