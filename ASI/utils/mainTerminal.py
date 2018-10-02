#!/usr/bin/env python
# -*- coding: utf-8 -*-
import globalVar
import fLogin
import dSignUp
import fMain
import dCreate
import dModify
import dNewComment
import dSearch

option = None

def execute_action(action, level):
	if action == 1:
		print "Choose search parameters."
		print dSearch.getTicketIDsList(globalVar.userLogged)
		id = raw_input("ID: ")
		id = None if (id == '') else int(id)
		print dSearch.getUsersList()
		creator = raw_input("Creator: ")
		creator = None if (creator == '') else creator
		responsible = raw_input("Responsible: ")
		responsible = None if (responsible == '') else responsible
		priority_list = ["Critica", "Grave", "Alta", "Media", "Baja"]
		print priority_list
		priority = raw_input("Priority: ")
		priority = None if (priority == '') else priority
		state_list = ["Inicio", "Asignado", "En proceso", "Finalizado"]
		print state_list
		state = raw_input("State: ")
		state = None if (state == '') else state
		search = dSearch.searchTicket(id, creator, responsible, priority, state)
		if search is not None:
			table = fMain.formatTableTerminal(search)
			return table
		else:
			return None
	elif action == 3:
		id = raw_input("Ticket ID: ")
		print fMain.showTicket(id)
	elif action == 4:
		desc = raw_input("Description: ")
		dCreate.addTicket(desc, globalVar.userLogged)
	elif action == 5:
		print dModify.getAssignedTicketList(globalVar.userLogged)
		id = int(raw_input("Choose ticket to modify: "))
		print "Ticket info"
		info = dModify.getTicketInfo(id)
		print info
		print dModify.getUserList()
		responsible = raw_input("Responsible: ")
		responsible = info[0] if (responsible == '') else responsible
		priority_list = ["Crítica", "Grave", "Alta", "Media", "Baja"]
		print priority_list
		priority = raw_input("Priority: ")
		priority = info[1] if (priority == '') else priority
		state_list = ["Inicio", "Asignado", "En proceso", "Finalizado"]
		print state_list
		state = raw_input("State: ")
		state = info[2] if (state == '') else state
		dModify.updateTicket(id, responsible, priority, state)
	elif action == 6:
		print dNewComment.getAssignedTicketList(globalVar.userLogged)
		id = int(raw_input("Choose ticket to modify: "))
		text = raw_input("Commentary: ")
		dNewComment.addComment(text, globalVar.userLogged, id)
	table = fMain.getTableContent(globalVar.userLogged, level)
	return table

while option != 0:
	print "1. Login"
	print "2. Sign Up"
	print "0. Exit"
	option = int(raw_input())
	
	if option == 1:
		username = raw_input("\nUsername: ")
		password = raw_input("Password: ")
		level = fLogin.checkLogin(username, password)
		if level is None:
			print "Username or password incorrect."
		else:
			globalVar.userLogged = username
			table = fMain.getTableContent(globalVar.userLogged, level)
			action = None
			while action != 0:
				if table is None:
					print "No tickets found."
				else:
					print table
				print "------------------"
				print "1. Search tickets"
				print "2. Show all tickets"
				print "3. Show ticket info"
				if level != 3:
					print "4. Create tickets"
				if level != 0:
					print "5. Modify ticket"
					print "6. Add commentary to ticket"
				print "0. Sign out"
				action = int(raw_input())
				if action != 0:
					table = execute_action(action, level)
	elif option == 2:
		work_list = dSignUp.getWorkList()
		print "\nWorks:"
		for work in work_list:
			print work,
		result = None
		while result is None:
			username = raw_input("\nUsername: ")
			password = raw_input("Password: ")
			workname = raw_input("Work: ")
			result = dSignUp.addUser(username, password, workname)
			if result is None:
				print "Already existing username."
	print "\n"
