from controllers import tournament
from controllers import home
from controllers import players


class Controller:

    __tournament_controller: tournament.TournamentController
    __home_controller: home.HomeController
    __players_controller: players.PlayersController

    def __init__(self):
        self.__tournament_controller = tournament.TournamentController()
        self.__home_controller = home.HomeController()
        self.__players_controller = players.PlayersController()

        while True:
            self.__tournament_controller._tournament = None
            self.__parse_user_action(self.__home_controller.input_home_menu())

    def __parse_user_action(self, action: int):
        if action == 1:
            self.__tournament_controller.create_new_tournament()
        elif action == 2:
            self.__players_controller.change_player_rank()
        elif action == 3:
            self.__tournament_controller.list_tournaments()
        elif action == 4:
            self.__tournament_controller.list_all_tournaments()
