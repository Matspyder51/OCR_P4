from views.tournament import tournament
from models.player import player
from models.tournament import tournament as tournament_model
from utils import to_boolean, ask_data


class TournamentController:

    _view: tournament.TournamentView
    _tournament: tournament_model.Tournament

    @property
    def players(self):
        return self._tournament.players

    def __init__(self):
        self._tournament = tournament_model.Tournament()
        self._view = tournament.TournamentView()

    def add_player(self, ply: player.Player, is_new: bool = False):
        self._tournament.add_player(ply)

        if is_new:
            ply.add_player_in_json()

        self._view.print_player_added(f"{ply.lastname} {ply.firstname}")

    def add_players_in_tournament(self):
        while len(self.players) != 8:
            is_new_player: bool = to_boolean(input("Is this a new player ? (Y/N) : "))
            lastname: str
            firstname: str
            sex: str
            birthdate: str
            rank: int = 0
            if is_new_player:
                lastname = input("Please enter player lastname : ")
                firstname = input("Please enter player firstname : ")
                sex = ask_data("Please enter player sex (M/F) : ", ["m", "f", "M", "F"])
                birthdate = input("Please enter player birthdate (DD/MM/YYYY) : ")

                self.add_player(
                    player.Player([lastname, firstname, birthdate, sex, rank]),
                    is_new_player,
                )
            else:
                # TODO: Move this to players controller
                search = input("Please enter player's name to find : ")
                possible_players = player.Player.get_player_from_name(search)
                if len(possible_players) < 1:
                    # TODO: Ask if he want to create a new one or find another name
                    continue
                self._view.print_players_list(possible_players)
                selected = int(input("Please enter the id of the player : "))
                final = next(x for x in possible_players if x.doc_id == selected)
                self.add_player(
                    player.Player(
                        [
                            final["lastname"],
                            final["firstname"],
                            final["birthdate"],
                            final["sex"],
                            final["rank"],
                            final.doc_id,
                        ]
                    ),
                    is_new_player,
                )

    def create_new_tournament(self):

        self._tournament.name = input("Please enter tournament name : ")

        self.add_players_in_tournament()

        self._tournament.save_tournament()
