from controllers.tournament import tournament
from controllers.home import home

class Controller:

	__tournament_controller: tournament.TournamentController
	__home_controller: home.HomeController

	def __init__(self):
		self.__tournament_controller = tournament.TournamentController()
		self.__home_controller = home.HomeController()

		self.__parse_user_action(self.__home_controller.input_home_menu())

	def __parse_user_action(self, action: int):
		if action == 1:
			self.__tournament_controller.create_new_tournament()