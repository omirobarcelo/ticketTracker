#!/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
import db_model

"""
Functions wich interact with the Rol table.
"""

def insert_rol(work, lvl):
	"""
	Inserts rol in table.
	
	:param work: Name of rol
	:type work: String
	:param level: Level of rol
	:type level: Integer
	
	:returns: Rol object, or None if IntegrityError
	"""
	try:
		rol = db_model.Rol.create(rolname=work, level=lvl)
		return rol
	except IntegrityError:
		print "insert_rol(): This rol already exists or none valid level."
		return None

def get_rol(rolname):
	"""
	Retrieves rol object from database.
	
	:param rolname: Name of the rol to retrieve
	:type rolname: String
	
	:returns: Rol object, or None if DoesNotExist
	"""
	try:
		rol = db_model.Rol.get(db_model.Rol.rolname == rolname)
		return rol
	except DoesNotExist:
		print "get_rol(): This rol is not registered in the database."
		return None

def get_all_registers(sort=False, value=None):
	"""
	Obtains all the registers of the Rol table. Admits a sorting option.
	
	:param sort: If True, will sort
	:type sort: Boolean
	:param value: By which field will be the registers sorted (rolname, level)
	:type value: String
	
	:returns: SelectQuery with the registers
	"""
	if sort == False:
		return db_model.Rol.select()
	else:
		if value == "rolname":
			return db_model.Rol.select().order_by(db_model.Rol.rolname)
		elif value == "level":
			return db_model.Rol.select().order_by(db_model.Rol.level)
		
def get_name(rol):
	"""
	Returns the name of a rol.
	
	:param rol: Rol object
	:type rol: Rol
	
	:returns: String
	"""
	return rol.rolname

def get_level(rol):
	"""
	Returns the level of a rol.
	
	:param rol: Rol object
	:type rol: Rol
	
	:returns: Integer
	"""
	return rol.level
