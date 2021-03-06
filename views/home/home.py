from colorama import Fore, Back, Style

class HomeView:

	def __init__(self):
		pass

	@staticmethod
	def print_start_message():
		print(f"Welcome in {Fore.GREEN}ChessTournamentManager {Fore.YELLOW}version 0.0.1")
	
	@staticmethod
	def print_home_menu():
		print("Type \"quit\" to exit the program")
		print("Home menu :")
		print(f"{Fore.RED}[1] {Fore.RESET}Create a new tournament")

	@staticmethod
	def print_home_menu_selection_error(error: str):
		print(f"{Fore.RED}Your entry is incorrect: {error}")
