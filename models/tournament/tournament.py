from models.player import player
from controllers.database import get_table


class Tournament:

    __id: int
    name: str
    place: str
    date: str
    round_amount: int = 4
    players: list
    description: str
    ended: bool = False

    def __init__(self):
        self.players = []

    def add_player(self, ply: player.Player):
        if self.players.count(ply) == 0:
            self.players.insert(len(self.players), ply)
        else:
            print("This player is already in tournament")

    def __get_players_ids(self):
        results = []
        for ply in self.players:
            results.insert(len(results), ply.get_id())

        return results

    def save_tournament(self):
        table = get_table("tournaments")
        if self.__id != None:
            # TODO: Update the document
            pass
        else:
            self.__id = table.insert(
                {
                    "name": self.name,
                    "description": self.description,
                    "place": self.place,
                    "date": self.date,
                    "round_amount": self.round_amount,
                    "players": self.__get_players_ids(),
                    "ended": self.ended,
                }
            )
