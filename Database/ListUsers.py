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
    
    c.execute("""SELECT gID, UID,name,mod_dt
                FROM users""")
    
    json_return = []
    i=0
    rows=c.rowcount
    
    for row in c:
        json_return[i] = {"gID": row[0],
            "UID":row[1],
        "name":row[2],
        "mod_dt":row[3]}
        ++i
    c.close()

    json.dumps(json_return)
        
    return json_return

