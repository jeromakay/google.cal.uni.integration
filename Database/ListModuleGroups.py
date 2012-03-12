'''
Created on 12 Márta 2012

@author: home
'''
import json
import sqlite3 as sqlite
#RETURNS A JSON STRING REPRESENTING ALL GROUPS IN THE DATABASE
def ListModuleGroups(database,module_id):
    
    connect=sqlite.connect(database)
    c=connect.cursor
    
    c.execute("""SELECT group_id
                FROM timetables
                WHERE module_id=?""",module_id)
    
    json_return = []
    i=0
    
    for row in c:
        json_return[i] = {"group_id": row[0]}
        ++i
    c.close()

    json.dumps(json_return)
        
    return json_return

