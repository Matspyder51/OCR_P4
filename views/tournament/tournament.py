from colorama import Fore
from models.tournament import Tournament


class TournamentView:
    def __init__(self):
        pass

    @staticmethod
    def print_player_added(name: str):
        print(f"{Fore.GREEN}Player added : {Fore.RESET}{name}")

    @staticmethod
    def print_error(error: str):
        print(f"{Fore.RED}Error: {Fore.RESET}{error}")

    @staticmethod
    def print_players_list(players: list):
        for ply in players:
            print(
                f"{ply.doc_id} - {ply['lastname']} {ply['firstname']} {ply['sex']} {ply['birthdate']}"
            )

    @staticmethod
    def print_matches_list(matches: list):
        i = 0
        for match in matches:
            text: str = ""
            text += f"{i} - "
            text += f"{match.upPlayer.lastname} {match.upPlayer.firstname} ({match.upPlayer.tournament_rank})"
            text += f" {Fore.YELLOW}versus {Fore.RESET}"
            text += f"{match.downPlayer.lastname} {match.downPlayer.firstname} ({match.downPlayer.tournament_rank})"
            if match.ended:
                text += f"{Fore.RED} (ENDED) {Fore.RESET}Winned by: {match.winnedBy}"
            print(text)
            i += 1

    @staticmethod
    def print_tournaments_list(tournaments: list):
        for trn in tournaments:
            print(f"{trn.doc_id} : {trn['name']} | {trn['date']}")

    @staticmethod
    def print_tournament_overview(tournament: Tournament):
        print("Tournament Overview:")
        print(f"\tName: {tournament.name}")
        print(f"\tPlace: {tournament.place}")
        print(f"\tDate: {tournament.date}")
        print(f"\tDescription: {tournament.description}")
        print(f"\tAmount of rounds: {tournament.round_amount}")