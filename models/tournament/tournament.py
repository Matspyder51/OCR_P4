from models.player import player

class Tournament:

	name: str
	place: str
	date: str
	round_amount: int
	players: list
	description: str

	def __init__(self):
		self.players = []

	def add_player(self, ply: player.Player):
		if self.players.count(ply) == 0:
			self.players.insert(len(self.players), ply)
		else:
			print('This player is already in tournament')