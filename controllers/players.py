from views.players import players
from models.player import Player


class PlayersController:

    _view: players.PlayersView

    def __init__(self):
        self._view = players.PlayersView()

    def change_player_rank(self):
        player_name = input("Please enter the name of the player to manage: ")
        possible_players = Player.get_player_from_name(player_name)
        self._view.print_players_list(possible_players)
        selected = int(input("Please enter the id of player to manage: "))
        _ply = possible_players[selected]

        ply = Player(
            [
                _ply["lastname"],
                _ply["firstname"],
                _ply["birthdate"],
                _ply["sex"],
                _ply["rank"],
            ],
            _ply.doc_id
        )
        new_rank = int(input("Please enter the new rank of the player: "))
        ply.rank = new_rank
        ply.update_in_json()
