class PlayersView:

    @staticmethod
    def print_players_list(players: list):
        """Print list of players"""
        i = 0
        for ply in players:
            print(f"{i} - {ply['lastname']} {ply['firstname']} {ply['sex']} {ply['birthdate']} {ply['rank']}")
            i += 1
