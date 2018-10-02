#!/usr/bin/env python
# -*- coding: utf-8 -*-
import db_fRol
import db_fUser
import db_fTicket

"""
Functions assigned to the Search ticket dialog.
"""

def getTicketIDsList(username):
	"""
	Obtains a sorted list of the ticket identifiers of the user's visible tickets.
	
	:param username: Username of the user
	:type username: String
	
	:returns: String List
	"""
	level = db_fRol.get_level(db_fUser.get_work(username))
	id_list = []
	ticket_list = None
	
	if level == 1 or level == 2:
		ticket_list = db_fTicket.get_all_registers()
	else:
		user = db_fUser.get_user(username)
		if level == 0:
			ticket_list = db_fUser.get_tickets_created(user)
		else:
			ticket_list = db_fUser.get_tickets_assigned(user)
	for ticket in ticket_list:
			id_list.append(str(db_fTicket.get_id(ticket)))
	id_list.sort()
	
	return id_list

def getUsersList():
	"""
	Obtains a sorted list of all the users usernames.
	
	:returns: String List
	"""
	user_list =  db_fUser.get_all_registers(sort=True, value='username')
	username_list = []
	
	for user in user_list:
		username_list.append(str(db_fUser.get_username(user)))
	
	return username_list

def searchTicket(id, creator_name, responsible_name, priority, state):
	"""
	Obtains a query with the tickets that fulfill the requirements.
	
	:param id: Ticket identifier
	:type if: Integer
	:param creator_name: Username of the creator user
	:type creator_name: String
	:param responsible_name: Username of the responsible user
	:type responsible_name: String
	:param priority: Priority of the ticket
	:type priority: String
	:param state: State of the ticket
	:type state: String
	
	:returns: Ticket SelectQuery
	"""
	creator = None if (creator_name is None) else db_fUser.get_user(creator_name)
	responsible = None if (responsible_name is None) else db_fUser.get_user(responsible_name)
	ticket_list = db_fTicket.select_ticket(id, creator, responsible, priority, state)
	
	return ticket_list
