'''
Created on 12 Márta 2012

@author: home
'''
import json
import sqlite3 as sqlite
#RETURNS A JSON STRING REPRESENTING ALL GROUPS IN THE DATABASE
def ListUsersGroups(database,user_id):
    
    connect=sqlite.connect(database)
    c=connect.cursor
    
    c.execute("""SELECT groups.group_id, groups.title,groups.description,groups.group_type_id,groups.mod_dt
                FROM groups,grouped_users
                WHERE groups.group_id = grouped_users.group_id
                    AND grouped_users.gID = ?""",user_id)
    
    json_return = []
    i=0
    
    for row in c:
        json_return[i] = {"id": row[0],
            "title":row[1],
        "description":row[2],
        "type_id":row[3],
        "mod_dt":row[4]}
        ++i
    c.close()

    json.dumps(json_return)
        
    return json_return

