#!/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
import db_model

"""
Script that creates all the database's tables.

Only used for one initial execution.
"""

db_model.Rol.create_table()
db_model.User.create_table()
db_model.Ticket.create_table()
db_model.Commentary.create_table()
