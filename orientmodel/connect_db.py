# In this file we connec to the database
import pyorient
# init a connection to the database

def connect(database,username,password,host):
	client = pyorient.OrientDB(host, 2424)
	session_id = client.connect( username, password)
	client.db_open( database, "admin", "admin")
	return client
