import gdata.gauth
import gdata.contacts.client
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom.data
import time
import data
import string
from uccal import login
from Database import DB

def addModule(Title, Summary):
	"""Creates a Google Calendar
		
		Args:
			Title: The Calendars name
			Summary: The description of the calendar
			
	"""

	#for hardcoded password + username
	calendar_client = login.adminLogin("calendar")
	
	Title = "UCC MODULE " + Title

	# Create the calendar
	calendar = gdata.calendar.data.CalendarEntry()
	calendar.title = atom.data.Title(text=Title)
	calendar.summary = atom.data.Summary(text=Summary)
	calendar.where.append(gdata.calendar.data.CalendarWhere(value='UCC'))
	calendar.color = gdata.calendar.data.ColorProperty(value='#333333')
	calendar.timezone = gdata.calendar.data.TimeZoneProperty(value='UTC')
	calendar.hidden = gdata.calendar.data.HiddenProperty(value='false')

	new_calendar = calendar_client.InsertCalendar(new_calendar=calendar)
	
	cal_id = new_calendar.id.text
	
	#this code can be used if you want cal_id not to include the preamble and consumer key
	cal_id = string.replace(cal_id, "http://www.google.com/calendar/feeds/default/calendars/", "")
	
	DB.CreateModule(cal_id, Title, Summary)
	
	return cal_id
	
def deleteModule(cal_id):
	"""Deletes a Google Calendar

		Args:
			cal_id: The Calendars ID

	"""
	cal_id = string.replace(cal_id, "@", "%40")
	cal_id_2 = "https://www.google.com/calendar/feeds/default/owncalendars/full/" + cal_id
	
	#for hardcoded password + username
	calendar_client = login.adminLogin("calendar")

	feed = calendar_client.GetOwnCalendarsFeed()
	
	for entry in feed.entry:
		if entry.GetEditLink().href == cal_id_2:
			calendar_client.Delete(entry.GetEditLink().href)
			
	DB.DeleteModule(cal_id)
			
def update(cal_id, Title, Summary):
	"""Deletes a Google Calendar

		Args:
			cal_id: The Calendars ID

	"""
	
	cal_id = "https://www.google.com/calendar/feeds/default/owncalendars/full/" + cal_id
	
	cal_id = string.replace(cal_id, "@", "%40")
	
	#for hardcoded password + username
	calendar_client = login.adminLogin("calendar")

	feed = calendar_client.GetOwnCalendarsFeed()
	for entry in feed.entry:
		if entry.GetEditLink().href == cal_id:
			# calendar represents a previously retrieved CalendarEntry
			entry.title = atom.data.Title(text=Title)
			entry.summary = atom.data.Summary(text=Summary)
			updated_calendar = calendar_client.Update(entry)
			
