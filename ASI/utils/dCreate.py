#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import db_fUser
import db_fTicket
import db_fJoin

"""
Functions assigned to the Create ticket dialog.
"""

def addTicket(description, createdBy):
	"""
	Adds a ticket in the database and it is automatically assigned to the least busy level 1 user.
	
	:param description: Text of the ticket to be added
	:type description: String
	:param createdBy: Username of the ticket creator
	:type createdBy: String
	"""
	level_list = db_fJoin.get_users_by_level(1)
	creator = db_fUser.get_user(createdBy)
	min = sys.maxint
	minIndex = 0
	
	for i, user in enumerate(level_list):
		value = db_fUser.count_tickets_assigned(user)
		if value < min:
			min = value
			minIndex = i
	db_fTicket.insert_ticket(description, creator, level_list[minIndex])
	# return ticket
