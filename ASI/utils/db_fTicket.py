#!/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
import db_model

"""
Functions wich interact with the User table.
"""

def insert_ticket(description, creator, responsible):
	"""
	Inserts ticket in table.
	
	:param description: Text of the ticket
	:type description: LongText
	:param creator: User who created the ticket
	:type creator: User
	:param responsible: User assigned to the ticket
	:type responsible: User
	
	:returns: Ticket object, or None if IntegrityError
	"""
	try:
		ticket = db_model.Ticket.create(description=description, creator=creator, responsible=responsible)
		return ticket
	except IntegrityError:
		print "insert_ticket(): This ticket already exists."
		return None

def get_ticket(id):
	"""
	Retrieves ticket object from database.
	
	:param id: Identifier of the ticket to retrieve
	:type id: Integer
	
	:returns: Ticket object, or None if DoesNotExist
	"""
	try:
		ticket = db_model.Ticket.get(db_model.Ticket.id == id)
		return ticket
	except DoesNotExist:
		print "get_ticket(): This ticket ID is not registered in the database."
		return None

def get_all_registers(sort=False, value=None):
	"""
	Obtains all the registers of the Ticket table. Admits a sorting option.
	
	:param sort: If True, will sort
	:type sort: Boolean
	:param value: By which field will be the registers sorted (id, createTime, creator, responsible, priority, state)
	:type value: String
	
	:returns: SelectQuery with the registers
	"""
	if sort == False:
		return db_model.Ticket.select()
	else:
		if value == "id":
			return db_model.Ticket.select().order_by(db_model.Ticket.id)
		elif value == "createTime":
			return db_model.Ticket.select().order_by(db_model.Ticket.createTime)
		elif value == "creator":
			return db_model.Ticket.select().order_by(db_model.Ticket.creator)
		elif value == "responsible":
			return db_model.Ticket.select().order_by(db_model.Ticket.responsible)
		elif value == "priority":
			return db_model.Ticket.select().order_by(db_model.Ticket.priority)
		elif value == "state":
			return db_model.Ticket.select().order_by(db_model.Ticket.state)

def select_ticket(id=None, creator=None, responsible=None, priority=None, state=None):
	"""
	Obtains a query of tickets which fulfill a list of requirments.
	
	:param id: Ticket identifier to search
	:type id: Integer
	:param creator: User to search as ticket creator
	:type creator: User
	:param responsible: User to search as ticket responsible
	:type responsible: User
	:param priority: Ticket priority to search
	:type priority: String
	:param state: Ticket state to search
	:type state: String
	
	:returns: SelectQuery with the registers
	"""
	ticket_list = db_model.Ticket.select()
	
	if id is not None:
		ticket_list = ticket_list.where(db_model.Ticket.id == id)
	if creator is not None:
		ticket_list = ticket_list.where(db_model.Ticket.creator == creator)
	if responsible is not None:
		ticket_list = ticket_list.where(db_model.Ticket.responsible == responsible)
	if priority is not None:
		ticket_list = ticket_list.where(db_model.Ticket.priority == priority)
	if state is not None:
		ticket_list = ticket_list.where(db_model.Ticket.state == state)
	
	if ticket_list.count() == 0:
		return None
	else:
		return ticket_list

def get_id(ticket):
	"""
	Returns the identifier of a ticket.
	
	:param ticket: Ticket object
	:type ticket: Ticket
	
	:returns: Integer
	"""
	return ticket.id

def get_responsible(ticket):
	"""
	Returns the responsible of a ticket.
	
	:param ticket: Ticket object
	:type ticket: Ticket
	
	:returns: User
	"""
	return ticket.responsible

def get_priority(ticket):
	"""
	Returns the priority of a ticket.
	
	:param ticket: Ticket object
	:type ticket: Ticket
	
	:returns: String
	"""
	return ticket.priority

def get_state(ticket):
	"""
	Returns the state of a ticket.
	
	:param ticket: Ticket object
	:type ticket: Ticket
	
	:returns: String
	"""
	return ticket.state

def update_responsible(ticket, new):
	"""
	Modifies the responsible field.
	
	:param ticket: Ticket to be modified
	:type ticket: Ticket
	:param new: New responsible
	:type new: User
	"""
	ticket.responsible = new
	ticket.save()

def update_priority(ticket, new):
	"""
	Modifies the priority field.
	
	:param ticket: Ticket to be modified
	:type ticket: Ticket
	:param new: New priority
	:type new: String
	"""
	ticket.priority = new
	ticket.save()

def update_state(ticket, new):
	"""
	Modifies the state field.
	
	:param ticket: Ticket to be modified
	:type ticket: Ticket
	:param new: New state
	:type new: String
	"""
	ticket.state = new
	ticket.save()

def info_ticket(ticket):
	"""
	Returns a list with the basic info (id, time created, responsible's username, priority, state, number of comments) of a ticket.
	
	:param ticket: Ticket object
	:type ticket: Ticket
	
	:returns: List
	"""
	ticket_info = []
	ticket_info.append(ticket.id)
	ticket_info.append(ticket.createTime)
	ticket_info.append(ticket.responsible.username)
	ticket_info.append(ticket.priority)
	ticket_info.append(ticket.state)
	ticket_info.append(ticket.comments.count())
	return ticket_info

def string_ticket(ticket):
	"""
	Formats and returns a string with all the info of a ticket.
	
	:param ticket: Ticket object
	:type ticket: Ticket
	
	:returns: String
	"""
	ticket_str_1 = """ID:            %d
Creation time: %s
Description:   %s
Creator:       %s
Responsible:   %s
Priority:      %s
State:         %s
Commentaries:
""" % (ticket.id, ticket.createTime, ticket.description, ticket.creator.username, ticket.responsible.username, ticket.priority, ticket.state)

	ticket_str_2 = ""
	for com in ticket.comments:
		ticket_str_2 += """	Author: %s
	Date:   %s
	Text:   %s
	
""" % (com.responsible.username, com.date, com.text)
	
	return (ticket_str_1 + ticket_str_2)

def print_ticket(ticket):
	"""
	Debug function. Prints ticket data (id, createTime, description, creator's username, responsible's username, priority, state, num. comments).
	
	:param ticket: Ticket whose data will be printed
	:type ticket: Ticket object
	"""
	if ticket is None:
		print "print_ticket(): Parameter is not a valid ticket."
	else:
		print "Id:         ", ticket.id
		print "Create time:", ticket.createTime
		print "Description:", ticket.description
		print "Creator:    ", ticket.creator.username
		print "Responsible:", ticket.responsible.username
		print "Priority:   ", ticket.priority
		print "State:      ", ticket.state
		print "Comments:   ", ticket.comments.count()
