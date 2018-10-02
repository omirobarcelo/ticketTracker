#!/usr/bin/env python
# -*- coding: utf-8 -*-
import db_fUser
import db_fTicket
import db_fComment

"""
Functions assigned to the New comment dialog.
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

def addComment(text, username, idTicket):
	"""
	Adds a comment in the database.
	
	:param text: Text of the comment to be added
	:type text: String
	:param username: Username of the comment writer
	:type username: String
	:param idTicket: Identifier of the ticket that owns the comment
	:type idTicket: Integer
	"""
	user = db_fUser.get_user(username)
	ticket = db_fTicket.get_ticket(idTicket)
	
	db_fComment.insert_comment(text, user, ticket)
