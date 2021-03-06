from controllers.database import get_table
from tinydb import Query

class Player:

	__id: int
	firstname: str
	lastname: str
	birthdate: str
	sex: str
	rank: int

	@property
	def get_id(self):
		return self.__id

	def __init__(self, data: list):
		self.lastname = data[0]
		self.firstname = data[1]
		self.birthdate = data[2]
		self.sex = data[3]
		self.rank = data[4]

	def update_in_json(self):
		table = get_table('players')
		ply = table.get(doc_id=self.__id)
		ply.update({'rank': self.rank})

	def add_player_in_json(self):
		table = get_table('players')
		id = table.insert({
			'firstname': self.firstname,
			'lastname': self.lastname,
			'birthdate': self.birthdate,
			'sex': self.sex,
			'rank': self.rank
		})
		self.__id = id

	@staticmethod
	def get_player_from_name(name: str):
		table = get_table('players')
		ply = Query()
		results = table.search(ply.firstname == name or ply.lastname == name)
		return results