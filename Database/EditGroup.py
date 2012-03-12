'''
Created on 12 Márta 2012

@author: home
'''
import sqlite3 as sqlite
#DELETES THE GROUP SPECIFIED BY Group_id OR Group_Name, RETURNS 1 IF SUCCESSFUL, 0 Otherwise
def EditGroup(database,
                 group_id,
                 title=None,
                 description=None,
                 group_type=None
                 ):
    
    connect=sqlite.connect(database)
    c=connect.cursor
    #finds the group to be modified
    c.execute("""SELECT title,description,group_type_id
                FROM groups
                WHERE group_id=?""",group_id)
    
    for row in c:
        if title is None:
            title=row[0]
        if description is None:
            description=row[1]
        if group_type is None:
            group_type=row[2]
    
    c.execute("""UPDATE groups
                SET title=?,description=?,group_type_id=?
                WHERE group_id=?""",title,description,group_type,group_id)
    
    connect.commit()
    c.close()


