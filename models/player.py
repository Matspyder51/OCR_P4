from controllers.database import get_table
from tinydb import Query


class Player:

    __id: int
    firstname: str
    lastname: str
    birthdate: str
    sex: str
    rank: int
    tournament_rank: float = 0.0

    @property
    def get_id(self):
        return self.__id

    def __init__(self, data: list, id: int = None, tournament_rank: int = 0.0):
        self.lastname = data[0]
        self.firstname = data[1]
        self.birthdate = data[2]
        self.sex = data[3]
        self.rank = data[4]
        self.tournament_rank = tournament_rank
        if id is not None:
            self.__id = id

    def update_in_json(self):
        table = get_table("players")
        table.update({"rank": self.rank}, doc_ids=[self.__id])

    def add_player_in_json(self):
        table = get_table("players")
        id = table.insert(
            {
                "firstname": self.firstname,
                "lastname": self.lastname,
                "birthdate": self.birthdate,
                "sex": self.sex,
                "rank": self.rank,
            }
        )
        self.__id = id

    def to_database(self, light: bool = False):
        if not light:
            return {
                "id": self.__id,
                "score": self.tournament_rank
            }
        else:
            return self.__id

    @staticmethod
    def get_player_from_name(name: str):
        table = get_table("players")
        ply = Query()

        def find_method(value):
            return value == name or value.find(name) != -1

        results = table.search(
            ply.firstname.test(find_method) | ply.lastname.test(find_method)
        )
        return results

    @staticmethod
    def get_player_from_id(id: int):
        table = get_table("players")

        return table.get(doc_id=id)
