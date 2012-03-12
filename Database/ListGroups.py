'''
Created on 12 Márta 2012

@author: home
'''
import json
import sqlite3 as sqlite
#RETURNS A JSON STRING REPRESENTING ALL GROUPS IN THE DATABASE
def ListGroups(database):
    
    connect=sqlite.connect(database)
    c=connect.cursor
    
    c.execute("""SELECT group_id, title,description,group_type_id,mod_dt,groups_gid
                FROM groups""")
    
    json_return = []
    i=0    
    for row in c:
        json_return[i] = {"id": row[0],
            "title":row[1],
        "description":row[2],
        "type_id":row[3],
        "mod_dt":row[4],
        "group_gid":row[5]}
        ++i
    c.close()

    json.dumps(json_return)
        
    return json_return

