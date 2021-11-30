from flask import Flask, g, request, current_app
import sqlite3

def get_message_db():
	"""
	This function handles creating the database of messages.
	It also creates a table messages if not existed.
	"""

	# check whether message_db is in g
	if "message_db" not in g: 
		g.message_db = sqlite3.connect("message_db.sqlite")

	# check whether the table messages is in message_db
	with current_app.open_resource('init.sql') as f:
		g.message_db.executescript(f.read().decode('utf8'))

	# return the connection g.message_db
	return g.message_db


def insert_message(request):
	"""
	This function handles inserting a user message into the database of messages.
	It also connects to the database with get_message_db(),
	and closes the connection once it's done.
	"""

	# get the variables from request
	name = request.form['name']
	message = request.form['message']
	# connect to database
	db = get_message_db()

	# add the variables to the database
	db.execute(
		'INSERT INTO messages (handle, message) VALUES (?, ?)',
		(name, message)
		)
	db.commit()

	# close connection to the database
	g.pop('message_db', None)
	db.close()


