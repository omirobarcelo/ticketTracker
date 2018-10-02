#!/usr/bin/env python
# -*- coding: utf-8 -*-
import db_fRol
import db_fUser

"""
Functions assigned to the Login frame.
"""

def checkLogin(username, password):
	"""
	Checks if username and password correct and returns level of user.
	
	:param username: Username of the user that wants to log in
	:type username: String
	:param password: Password of the user that wants to log in
	:type password: String
	
	:returns: Integer
	"""
	if db_fUser.check_password(username, password):
		return db_fRol.get_level(db_fUser.get_work(username))
	else:
		return None
