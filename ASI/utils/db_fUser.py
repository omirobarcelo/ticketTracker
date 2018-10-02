#!/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
import db_model

"""
Functions wich interact with the User table.
"""

def insert_user(name, password, rol):
	"""
	Inserts user in table.
	
	:param name: Name of the user in application
	:type name: String
	:param password: Password of the user in application
	:type password: String
	:param rol: Work of the user
	:type rol: Rol
	
	:returns: User object, or None if IntegrityError
	"""
	try:
		user = db_model.User.create(username=name, password=password, work=rol)
		return user
	except IntegrityError:
		print "insert_user(): This user already exists."
		return None

def get_user(username):
	"""
	Retrieves user object from database.
	
	:param username: Username of the user to retrieve
	:type username: String
	
	:returns: User object, or None if DoesNotExist
	"""
	try:
		user = db_model.User.get(db_model.User.username == username)
		return user
	except DoesNotExist:
		print "get_user(): This username is not registered in the database."
		return None

def get_all_registers(sort=False, value=None):
	"""
	Obtains all the registers of the User table. Admits a sorting option.
	
	:param sort: If True, will sort
	:type sort: Boolean
	:param value: By which field will be the registers sorted (username, work)
	:type value: String
	
	:returns: SelectQuery with the registers
	"""
	if sort == False:
		return db_model.User.select()
	else:
		if value == "username":
			return db_model.User.select().order_by(db_model.User.username)
		elif value == "work":
			return db_model.User.select().order_by(db_model.User.work)

def get_username(user):
	"""
	Returns the name of a user.
	
	:param user: User object
	:type user: User
	
	:returns: String
	"""
	return user.username
	
def get_work(username):
	"""
	Returns the work of a user.
	
	:param username: Username of the user
	:type username: String
	
	:returns: Rol object
	"""
	user = get_user(username)
	return user.work

def get_tickets_created(user):
	"""
	Obtains the tickets created by a user.
	
	:param user: User whose created tickets are to be retrieved
	:type user: User object
	
	:returns: SelectQuery with the tickets created by the user
	"""
	return user.created

def count_tickets_created(user):
	"""
	Obtains the number of tickets created by a user.
	
	:param user: User whose created tickets are to be counted
	:type user: User object
	
	:returns: Integer with the number of tickets created by the user
	"""
	return user.created.count()

def get_tickets_assigned(user):
	"""
	Obtains the tickets assigned to a user.
	
	:param user: User whose assigned tickets are to be retrieved
	:type user: User object
	
	:returns: SelectQuery with the tickets assigned to the user
	"""
	return user.assigned

def count_tickets_assigned(user):
	"""
	Obtains the number of tickets assigned to a user.
	
	:param user: User whose assigned tickets are to be counted
	:type user: User object
	
	:returns: Integer with the number of tickets assigned to the user
	"""
	return user.assigned.count()

def check_password(username, password):
	"""
	Checks if the parameteres are of a valid user.
	
	:param username: Username that is going to be checked
	:type username: String
	:param password: Password that is going to be checked
	:type password: String
	
	:returns: True if username and password match, False if it does not match and None if user does not exist
	"""
	user = get_user(username)
	if user is None:
		return None
	else:
		return user.password == password

def print_user(user):
	"""
	Debug function. Prints user data (username, password, work, num. assigned tickets).
	
	:param user: User whose data will be printed
	:type user: User object
	"""
	if user is None:
		print "print_user(): Parameter is not a valid user."
	else:
		print "Username:", user.username
		print "Password:", user.password
		print "Rol:     ", user.work.rolname
		print "Assigned:", user.assigned.count()
