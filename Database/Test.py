#coding=utf-8
'''
Created on 12 M�rta 2012
'''
import unittest
import simplejson as json
from Database import DB
class Test(unittest.TestCase):


    def test_make_group(self):
        DB.CreateGroupType('Everyone','The type containing everyone because homogenous groups is in right now')
        group_types=json.loads(DB.ListGroupTypes())['results']
        new_groups_id=0
        for group_type in group_types:
            if group_type['name']=='Everyone':
                new_groups_id=group_type['id']
        DB.CreateGroup(1, 'Test group Alpha', 'The first of many groups to come',new_groups_id)
        group_info=json.loads(DB.ListGroups())['results']
        is_test_group_there=False
        for group in group_info:
            if group['title'] == 'Test group Alpha':
                is_test_group_there=True
        self.assertTrue(is_test_group_there)
        
    def test_make_user(self):
        DB.CreateUser('0', '0', 'Herp Derpington')
        user_list=json.loads(DB.ListUsers())['results']

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.Creation']
    unittest.main()