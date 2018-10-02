#!/usr/bin/env python
# -*- coding: utf-8 -*-
import db_fUser
import db_fTicket

"""
Functions assigned to the Modify ticket dialog.
"""

def getAssignedTicketList(username):
	"""
	Obtains a sorted list of the identifiers of the user's assigned tickets.
	
	:param username: Username of the user to get its assigned tickets
	:type username: String
	
	:returns: String List
	"""
	user = db_fUser.get_user(username)
	ticket_list = db_fUser.get_tickets_assigned(user)
	id_list = []
	
	for ticket in ticket_list:
		id_list.append(str(db_fTicket.get_id(ticket)))
	id_list.sort()
	
	return id_list

def getUserList():
	"""
	Obtains a sorted list of all the users usernames.
	
	:returns: String List
	"""
	user_list = db_fUser.get_all_registers(sort=True, value="username")
	username_list = []
	
	for user in user_list:
		username_list.append(str(db_fUser.get_username(user)))
	# username_list.sort()
	
	return username_list

def getTicketInfo(id):
	"""
	Obtains a list of the responsible's username, priority and state of a ticket.
	
	:param id: Ticket identifier
	:type id: Integer
	
	:returns: String List
	"""
	ticket = db_fTicket.get_ticket(id)
	info = []
	
	info.append(str(db_fUser.get_username(db_fTicket.get_responsible(ticket))))
	info.append(str(db_fTicket.get_priority(ticket)))
	info.append(str(db_fTicket.get_state(ticket)))
	
	return info

def updateTicket(id, responsible, priority, state):
	"""
	Modifies a ticket.
	
	:param id: Ticket identifier to be modified
	:type id: Integer
	:param responsible: Username of the new user assigned to the ticket
	:type responsible: String
	:param priority: New priority
	:type priority: String
	:param state: New state
	:type state: String
	"""
	ticket = db_fTicket.get_ticket(id)
	user = db_fUser.get_user(responsible)
	
	db_fTicket.update_responsible(ticket, user)
	db_fTicket.update_priority(ticket, priority)
	db_fTicket.update_state(ticket, state)
