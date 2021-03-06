from tinydb import TinyDB

def get_database():
	return TinyDB('database.json')

def get_table(name: str):
	return get_database().table(name)