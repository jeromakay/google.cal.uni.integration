#!/usr/bin/python
#
# Copyright (C) 2009 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import gdata.gauth
import gdata.contacts.client
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom.data
import time

SOURCE_APP_NAME = 'addcaltwj3'

CONSUMER_KEY = 'jeromakay.com'
CONSUMER_SECRET = '4F9NldoELocv9RWI0esKSqMv'

requestor_id = 'twj2@' + CONSUMER_KEY
two_legged_oauth_token = gdata.gauth.TwoLeggedOAuthHmacToken(
	CONSUMER_KEY, CONSUMER_SECRET, requestor_id)

contacts_client = gdata.contacts.client.ContactsClient(source=SOURCE_APP_NAME)
contacts_client.auth_token = two_legged_oauth_token

calendar_client = gdata.calendar.client.CalendarClient()
calendar_client.auth_token = two_legged_oauth_token


calendar = gdata.calendar.data.CalendarEntry()
calendar.id = atom.data.Id(text='ml_8842_%4dunster#sports@group.v.calendar.google.com')
returned_calendar = calendar_client.InsertCalendarSubscription(calendar)