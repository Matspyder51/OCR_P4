from models.player import Player
import datetime


class Match:

    upPlayer: Player
    downPlayer: Player
    ended: bool = False
    winnedBy: int = None
    startTime: float = datetime.datetime.now().timestamp()
    endTime: float = None

    def __init__(self, upPlayer: Player = None, downPlayer: Player = None):
        self.upPlayer = upPlayer
        self.downPlayer = downPlayer

    def __eq__(self, other):
        if (
            self.upPlayer == other.upPlayer and self.downPlayer == other.downPlayer
        ) or (self.upPlayer == other.downPlayer and self.downPlayer == other.upPlayer):
            return True
        else:
            return False

    def to_dict(self):
        return {
            "upPlayer": self.upPlayer.to_database(True),
            "downPlayer": self.downPlayer.to_database(True),
            "ended": self.ended,
            "winnedBy": self.winnedBy,
            "startedAt": self.startTime,
            "endedAt": self.endTime
        }

    @staticmethod
    def from_dict(upPlayer: Player, downPlayer: Player, data):
        match = Match()
        match.ended = data["ended"]
        match.winnedBy = data["winnedBy"]
        match.startTime = data["startedAt"]
        match.endTime = data["endedAt"]
        match.upPlayer = upPlayer
        match.downPlayer = downPlayer

        return match