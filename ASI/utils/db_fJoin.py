#!/usr/bin/env python
# -*- coding: utf-8 -*-
import db_model
import db_fRol
import db_fUser
import db_fTicket

"""
Functions wich interact with more than one table.
"""

def get_users_by_level(level):
	"""
	Obtains query with all users of one level.
	
	:param level: Level of users to be retrieved
	:type level: Integer
	
	:returns: User SelectQuery
	"""
	query = db_model.User.select(db_model.User, db_model.Rol).join(db_model.Rol).where(db_model.Rol.level == level)
	return query
