'''
Created on 12 Márta 2012

@author: home
'''
import json
import sqlite3 as sqlite
#RETURNS A JSON STRING REPRESENTING ALL GROUPS IN THE DATABASE
def ListUsersModules(database,user_id):
    
    connect=sqlite.connect(database)
    c=connect.cursor
    
    c.execute("""SELECT modules.module_id, modules.title,modules.description,modules.google_cal_id,modules.mod_dt
                FROM grouped_users,timetables,modules
                WHERE timetables.group_id = grouped_users.group_id
                    AND timetables.module_id = modules.module_id
                    AND grouped_users.gID = ?""",user_id)
    
    json_return = []
    i=0
    
    for row in c:
        json_return[i] = {"id": row[0],
            "title":row[1],
        "description":row[2],
        "cal_id":row[3],
        "mod_dt":row[4]}
        ++i
    c.close()

    json.dumps(json_return)
        
    return json_return

