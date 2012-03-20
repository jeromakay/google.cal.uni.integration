#coding=utf-8
from google.appengine.ext import db



class GroupType(db.Model):
    title=db.StringProperty()
    group_type_id=db.IntegerProperty()
    description=db.StringProperty()
    
    
  
class Group(db.Model):
    group_gid=db.StringProperty()
    group_id=db.IntegerProperty()
    title=db.StringProperty()
    description=db.StringProperty()
    mod_dt=db.DateTimeProperty()
    
    group_type=db.ReferenceProperty(GroupType)
    
    group_modules=db.ListProperty(db.Key)
    
    @property
    def users(self):
        return User.gql("WHERE users_groups=:1",self.key())
    
class Module(db.Model):
    google_cal_id=db.StringProperty()
    module_id=db.IntegerProperty()
    title=db.StringProperty()
    description=db.StringProperty()
    mod_dt=db.DateTimeProperty()
    @property
    def groups(self):
        return Group.gql("WHERE group_modules=:1",self.key())
    
class User(db.Model):
    gID=db.StringProperty()
    uID=db.StringProperty()
    user_id=db.IntegerProperty()
    name=db.StringProperty()
    mod_dt=db.DateTimeProperty()
    
    users_groups=db.ListProperty(db.Key)