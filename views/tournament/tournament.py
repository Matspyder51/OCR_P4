from colorama import Fore, Back, Style
from controllers.tournament import tournament

class TournamentView:

	def __init__(self):
		pass

	@staticmethod
	def print_player_added(name: str):
		print(f"{Fore.GREEN}Player added : {Fore.RESET}{name}")

	@staticmethod
	def print_players_list(players: list):
		for ply in players:
			print(f"{ply.doc_id} - {ply['lastname']} {ply['firstname']} {ply['sex']} {ply['birthdate']}")