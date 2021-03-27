class PlayersView:

	def __init__(self):
		pass

	@staticmethod
	def print_players_list(players: list):
		i = 0
		for ply in players:
			print(f"{i} - {ply['lastname']} {ply['firstname']} {ply['sex']} {ply['birthdate']} {ply['rank']}")
			i += 1