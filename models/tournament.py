from models import player
from models.match import Match
from controllers.database import get_table
from tinydb import Query


class Tournament:

    __id: int = None
    name: str = ""
    place: str = ""
    date: str = ""
    round_amount: int = 4
    players: list = []
    description: str = ""
    current_round: int = -1
    matches: list = []
    ended: bool = False

    def __init_players_from_indices(self, data):
        for ply in data:
            ply_data = player.Player.get_player_from_id(ply["id"])
            self.players.insert(len(self.players), player.Player(
                [
                    ply_data["lastname"],
                    ply_data["firstname"],
                    ply_data["birthdate"],
                    ply_data["sex"],
                    ply_data["rank"],
                ],
                ply_data.doc_id,
                ply["score"]
            ))

    def load_from_database(self, data):
        self.__id = data.doc_id
        self.name = data["name"]
        self.place = data["place"]
        self.date = data["date"]
        self.round_amount = data["round_amount"]
        self.description = data["description"]
        self.current_round = data["current_round"]
        self.ended = data["ended"]

        self.__init_players_from_indices(data["players"])

        i = 0
        for rnd in data["matches"]:
            self.matches.insert(i, [])
            for match in rnd:
                self.matches[i].insert(len(self.matches[i]), Match.from_dict(self.__get_ply_from_id(match["upPlayer"]), self.__get_ply_from_id(match["downPlayer"]), match))
            i += 1

    def add_player(self, ply: player.Player):
        if self.players.count(ply) == 0:
            self.players.insert(len(self.players), ply)
        else:
            print("This player is already in tournament")

    def __get_players_infos(self):
        results = []
        for ply in self.players:
            results.insert(len(results), ply.to_database())

        return results

    def __get_matches(self):
        results = []
        for i in range(len(self.matches)):
            results.insert(i, [])
            for match in self.matches[i]:
                results[i].insert(len(results[i]), match.to_dict())

        return results

    def __get_ply_from_id(self, id):
        for ply in self.players:
            if ply.get_id == id:
                return ply

    def save_tournament(self):
        table = get_table("tournaments")

        data = {
            "name": self.name,
            "description": self.description,
            "place": self.place,
            "date": self.date,
            "round_amount": self.round_amount,
            "players": self.__get_players_infos(),
            "current_round": self.current_round,
            "matches": self.__get_matches(),
            "ended": self.ended,
        }

        if self.__id is not None:
            table.update(data, doc_ids=[self.__id])
        else:
            self.__id = table.insert(data)

    def is_all_matches_of_round_ended(self):
        if self.current_round == -1 or len(self.matches[self.current_round]) == 0:
            return True

        for match in self.matches[self.current_round]:
            if not match.ended:
                return False

        return True

    @staticmethod
    def get_tournaments():
        table = get_table("tournaments")
        trn = Query()

        results = table.search(trn.ended == False)

        return results
