#!/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
import db_model

"""
Functions wich interact with the User table.
"""

def insert_comment(text, responsible, ticket):
	"""
	Inserts comment in table.
	
	:param text: Text of the comment
	:type text: LongText
	:param responsible: User who wrote the comment
	:type responsible: User
	:param ticket: Ticket that owns the comment
	:type ticket: Ticket
	
	:returns: Comment object, or None if IntegrityError
	"""
	try:
		comment = db_model.Commentary.create(text=text, responsible=responsible, idTicket=ticket)
		return comment
	except IntegrityError:
		print "insert_comment(): This commentary already exists."
		return None

def get_comment(id):
	"""
	Retrieves comment object from database.
	
	:param id: Identifier of the comment to retrieve
	:type id: Integer
	
	:returns: Comment object, or None if DoesNotExist
	"""
	try:
		comment = db_model.Commentary.get(db_model.Commentary.id == id)
		return comment
	except DoesNotExist:
		print "get_comment(): This commentary ID is not registered in the database."
		return None

def print_comment(comment):
	"""
	Debug function. Prints comment data (id, date, text, responsible's username, ticket ID).
	
	:param comment: Comment whose data will be printed
	:type comment: Comment object
	"""
	if comment is None:
		print "print_comment(): Parameter is not a valid commentary."
	else:
		print "Id:       ", comment.id
		print "Date:     ", comment.date
		print "Text:     ", comment.text
		print "Author:   ", comment.responsible.username
		print "Ticket ID:", comment.idTicket.id
