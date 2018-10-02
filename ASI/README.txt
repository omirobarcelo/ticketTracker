	To execute:
- Open command line
- Move to TMS/ directory
- Execute ./main

	Dependencies (if needed):
- Python
- PySide (sudo apt-get install python-pyside)
- Peewee (sudo pip install peewee)

	Docs:
Main HTML with index found at:
/ASI/docs/_build/html/modules.html

	ASI.db Database Content:
Rol:
rolname, level
Conserje, 0
Recepctionista, 1
Limpiador, 1
Cocinero, 1
Informatico, 2
Mecanico, 2
Electricista, 2
Distribuidor, 3

User:
username, password, work.rolname
u0, 1234, Conserje
u1a, 1234, Recepcionista
u1b, 1234, Limpiador
u1c, 1234, Cocinero
u2a, 1234, Informatico
u2b, 1234, Mecanico
u2c, 1234, Electricista
u3, 1234, Distribuidor

Ticket:
id, description, creator.username, responsible.username, priority, state
1, Test Ticket 1, u0, u1a, Baja, Asignado
2, Test Ticket 2, u1a, u2a, Alta, Finalizado
3, Test Ticket 3, u0, u2c, Media, En proceso
4, Test Ticket 4, u0, u1b, Baja, Asignado
5, Test Ticket 5, u2b, u3, Critica, En proceso
6, Test Ticket 6, u0, u1c, Baja, Inicio
7, Test Ticket 7, u0, u1a, Baja, Inicio

Commentary:
id, text, responsible.username, idTicket.id
1, Test Comment 1, u1a, 1
2, Test Comment 2, u2c, 3
3, Test Comment 3, u2a, 5
4, Test Comment 4, u3, 5