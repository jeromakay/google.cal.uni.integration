import gdata.gauth
import gdata.contacts.client
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom.data
import time
import data
import string

def add(Title, Summary):
	"""Creates a Google Calendar
		
		Args:
			Title: The Calendars name
			Summary: The description of the calendar
			
	"""

	#for hardcoded password + username
	calendar_client = gdata.calendar.client.CalendarClient(source=data.SOURCE_APP_NAME)
	calendar_client.ClientLogin(data.ADMIN_EMAIL, data.ADMIN_PASSWORD, source ='apps')

	# Create the calendar
	calendar = gdata.calendar.data.CalendarEntry()
	calendar.title = atom.data.Title(text=Title)
	calendar.summary = atom.data.Summary(text=Summary)
	calendar.where.append(gdata.calendar.data.CalendarWhere(value='UCC'))
	calendar.color = gdata.calendar.data.ColorProperty(value='#333333')
	calendar.timezone = gdata.calendar.data.TimeZoneProperty(value='UTC')
	calendar.hidden = gdata.calendar.data.HiddenProperty(value='false')

	new_calendar = calendar_client.InsertCalendar(new_calendar=calendar)
	
def delete(cal_id):
	"""Deletes a Google Calendar

		Args:
			cal_id: The Calendars ID

	"""
	
	cal_id = "https://www.google.com/calendar/feeds/default/owncalendars/full/" + cal_id
	
	#for hardcoded password + username
	calendar_client = gdata.calendar.client.CalendarClient(source=data.SOURCE_APP_NAME)
	calendar_client.ClientLogin(data.ADMIN_EMAIL, data.ADMIN_PASSWORD, source ='apps')

	feed = calendar_client.GetOwnCalendarsFeed()
	for entry in feed.entry:
		if entry.GetEditLink().href == cal_id:
			calendar_client.Delete(cal_id)
			
def update(cal_id, Title, Summary):
	"""Deletes a Google Calendar

		Args:
			cal_id: The Calendars ID

	"""
	
	cal_id = "https://www.google.com/calendar/feeds/default/owncalendars/full/" + cal_id
	
	cal_id = string.replace(cal_id, "@", "%40")
	
	#for hardcoded password + username
	calendar_client = gdata.calendar.client.CalendarClient(source=data.SOURCE_APP_NAME)
	calendar_client.ClientLogin(data.ADMIN_EMAIL, data.ADMIN_PASSWORD, source ='apps')

	feed = calendar_client.GetOwnCalendarsFeed()
	for entry in feed.entry:
		if entry.GetEditLink().href == cal_id:
				# calendar represents a previously retrieved CalendarEntry
				entry.title = atom.data.Title(text=Title)
				entry.summary = atom.data.Summary(text=Summary)
				updated_calendar = calendar_client.Update(entry)
			
