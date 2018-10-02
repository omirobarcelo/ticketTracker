#!/usr/bin/env python
# -*- coding: utf-8 -*-
import db_fUser
import db_fTicket

"""
Functions assigned to the Main frame.
"""

def getTableContent(username, level):
	"""
	Obtains the tickets of the user logged in depending of its level and sorts them by time created if user is level 1, by priority if user is level 2 and by identifier if user is level 0 or 3.
	
	:param username: Username of the user whose tickets we are retrieving
	:type username: String
	:param level: Level of the user whose tickets we are retrieving
	:type level: Integer
	
	:returns: `Depends on format needed`
	"""
	ticket_list = None
	
	if level == 1:
		ticket_list = db_fTicket.get_all_registers(sort=True, value='createTime')
	elif level == 2:
		ticket_list = db_fTicket.get_all_registers(sort=True, value='priority')
	else:
		user = db_fUser.get_user(username)
		if level == 0:
			ticket_list = db_fUser.get_tickets_created(user)
		else:
			ticket_list = db_fUser.get_tickets_assigned(user)
	# Depending on info needed for QT Table #
	# table_content = formatTableTerminal(ticket_list)
	header, table_content = formatTableGraphic(ticket_list)
	
	return (header, table_content)
	#########################################

def formatTableGraphic(ticket_list):
	header = ["ID", "Creation time", "Responsible", "Priority", "State", "Commentaries"]
	table_info = []
	for ticket in ticket_list:
		info = db_fTicket.info_ticket(ticket)
		table_info.append(info)
	return (header, table_info)

def formatTableTerminal(ticket_list):
	"""
	Command line function. Formats a ticket list in a text table.
	
	:param ticket_list: List of tickets to be formatted
	:type ticket_list: List or SelectQuery
	
	:returns: String
	"""
	str = "%-5s %-20s %-12s %-9s %-12s %-18s\n" % ("ID", "Creation time", "Responsible", "Priority", "State", "Num. Commentaries")
	for ticket in ticket_list:
		info = db_fTicket.info_ticket(ticket)
		str += "%-5d %-20s %-12s %-9s %-12s %-18d\n" % (info[0], info[1], info[2], info[3], info[4], info[5])
	
	return str

def showTicket(id):
	"""
	Formats a ticket in a visual shown info.
	
	:param id: Ticket identifier
	:type id: Integer
	
	:returns: String
	"""
	ticket = db_fTicket.get_ticket(id)
	str = db_fTicket.string_ticket(ticket)
	return str
