#!/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
import time
import datetime

"""Database definition

.. figure:: docs/modelUML.png
	:width: 542px
	:align: left
	:height: 344px
	:alt: ASI.db UML model
	:figclass: align-center
	
	ASI.db database UML model

"""
#asi_dbase = MySQLDatabase('ASI.db')
asi_dbase = SqliteDatabase('ASI.db')

class BaseModel(Model):
	"""
	Class required when using `Peewee ORM <docs.peewee-orm.com/en/latest/>`_.
	
	Selects database to use.
	"""
	class Meta:
		database = asi_dbase

class Rol(BaseModel):
	"""
	Rols available for a user.
	
	:rolname: string -- Work's name.
	:level: integer -- Work's level in USC (User Service Center). From 0 to 3.
	"""
	rolname = CharField(primary_key=True)
	level = IntegerField(index=True, constraints=[Check('level >= 0 and level <= 3')])

class User(BaseModel):
	"""
	Users registered in USC's application.
	
	:username: string -- User's name in the application.
	:password: string -- User's password to safely login.
	:work: foreign key(Rol) -- User's rol. Reference name: *names*
	"""
	username = CharField(max_length=24, index=True, primary_key=True)
	password = CharField()
	work = ForeignKeyField(Rol, related_name='names')
	
class Ticket(BaseModel):
	"""
	Tickets created.
	
	:id: unique -- Ticket ID.
	:createTime: date time -- Ticket's date and time creation.
	:description: text -- Ticket's description by creator.
	:creator: foreign key(User) -- User who created the ticket. Reference name: *created*
	:responsible: foreign key(User) -- User assigned to the ticket. Reference name: *assigned*
	:priority: string -- Range of values [Crítca, Grave, Alta, Media, Baja]
	:state: string -- Range of value [Inicio, Asignado, En proceso, Finalizado]
	"""
	id = PrimaryKeyField(index=True)
	createTime = DateTimeField(default=time.strftime('%Y-%m-%d %H:%M:%S'), index=True)
	description = TextField()
	creator = ForeignKeyField(User, related_name='created')
	responsible = ForeignKeyField(User, related_name='assigned')
	priority = CharField(default="Baja", constraints=[Check('priority == "Critica" or priority == "Grave" or priority == "Alta" or priority == "Media" or priority == "Baja"')])
	state = CharField(default="Inicio", constraints=[Check('state == "Inicio" or state == "Asignado" or state == "En proceso" or state == "Finalizado"')])

class Commentary(BaseModel):
	"""
	Commentary of a ticket.
	
	:id: unique -- Commentary ID.
	:date: date time -- Commentary's date and time redaction.
	:text: text -- Commentary's test written by responsible.
	:responsible: foreign key(User) -- User who wrote the commentary. Reference name: *written*
	:idTicket: foreign key(Ticket) -- Ticket to which belongs the commentary. Reference name: *comments*
	"""
	id = PrimaryKeyField(index=True)
	date = DateTimeField(default=time.strftime('%Y-%m-%d %H:%M:%S'), index=True)
	text = TextField()
	responsible = ForeignKeyField(User, related_name='written')
	idTicket = ForeignKeyField(Ticket, related_name='comments')
