'''
Created on 12 Márta 2012

@author: home
'''
import json
import sqlite3 as sqlite
#RETURNS A JSON STRING REPRESENTING ALL MODULES IN THE DATABASE
def ListModules(database):
    
    connect=sqlite.connect(database)
    c=connect.cursor
    
    c.execute("""SELECT module_id,google_cal_id,title,description,mod_dt
                FROM modules""")
    
    json_return = []
    i=0
    
    for row in c:
        json_return[i] = {"id": row[0],
            "cal_id":row[1],
        "title":row[2],
        "description":row[3],
        "mod_dt":row[4]}
        ++i
    c.close

    json.dumps(json_return)
        
    return json_return

