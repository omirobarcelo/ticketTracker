#!/usr/bin/env python
# -*- coding: utf-8 -*-
import db_fRol
import db_fUser

"""
Functions assigned to the Sign Up dialog.
"""

def getWorkList():
	"""
	Obtains a list with the name of all the rols in the database sorted by name.
	
	:returns: String List
	"""
	rol_list = db_fRol.get_all_registers(sort=True, value="rolname")
	work_list = []
	
	for rol in rol_list:
		work_list.append(str(db_fRol.get_name(rol)))
	# work_list.sort()
	
	return work_list

def addUser(username, password, workname):
	"""
	Adds a user in the database.
	
	:param username: Username of the user
	:type username: String
	:param password: Password of the user
	:type password: String
	:param workname: Name of the rol selected by the user
	:type workname: String
	
	:returns: User object, or None if error
	"""
	rol = db_fRol.get_rol(workname)
	user = db_fUser.insert_user(username, password, rol)
	return user
