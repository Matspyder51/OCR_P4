from colorama import Fore
from models.tournament import Tournament
import datetime


class TournamentView:
    def __init__(self):
        pass

    @staticmethod
    def print_player_added(name: str):
        """Print a message indicating than a player has been added to the tournament"""
        print(f"{Fore.GREEN}Player added : {Fore.RESET}{name}")

    @staticmethod
    def print_error(error: str):
        """Print an error to the user"""
        print(f"{Fore.RED}Error: {Fore.RESET}{error}")

    @staticmethod
    def print_players_list(players: list):
        """Print list of players"""
        for ply in players:
            print(
                f"{ply.doc_id} - {ply['lastname']} {ply['firstname']} {ply['sex']} {ply['birthdate']}"
            )

    @staticmethod
    def print_matches_list(matches: list, round_number: int):
        """Print matchs list of current round"""
        i = 0
        print(f"Round number {round_number + 1} :")
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
        """Print list of tournaments"""
        for trn in tournaments:
            print(f"{trn.doc_id} : {trn['name']} | {trn['date']}")

    @staticmethod
    def print_matches(matches: list, indent: str = ""):
        """Print list of matches"""
        for match in matches:
            text = indent
            text += f"{Fore.GREEN if match.winnedBy == 0 else Fore.RED}"
            text += f" {match.upPlayer.lastname} {match.upPlayer.firstname}"
            text += f" {Fore.BLUE}versus{Fore.RESET}"
            text += f"{Fore.GREEN if match.winnedBy == 1 else Fore.RED}"
            text += f" {match.downPlayer.lastname} {match.downPlayer.firstname}"
            text += f"{Fore.RESET} Start: {datetime.datetime.fromtimestamp(match.startTime)}"
            if match.endTime is not None:
                text += f" Ended: {datetime.datetime.fromtimestamp(match.endTime)}"
            print(text)

    @staticmethod
    def print_tournament_overview(
        tournament: Tournament, action: int = -1, sortType: int = -1
    ):
        """Manage tournament overview"""
        if action == -1:
            print("Tournament Overview:")
            print(f"\tName: {tournament.name}")
            print(f"\tPlace: {tournament.place}")
            print(f"\tDate: {tournament.date}")
            print(f"\tDescription: {tournament.description}")
            print(f"\tAmount of rounds: {tournament.round_amount}")
        elif action == 0:
            _temp_players = tournament.players.copy()
            print("Players:")
            if sortType == 0:
                _temp_players.sort(
                    key=lambda x: (x.lastname.lower(), x.firstname.lower())
                )
            elif sortType == 1:
                _temp_players.sort(key=lambda x: x.rank)
            for ply in _temp_players:
                print(
                    f"\t{ply.lastname} {ply.firstname} {ply.birthdate} {ply.sex} {ply.rank} {ply.tournament_rank}"
                )

        elif action == 1:
            print("Matchs:")
            for rnd_number, rnd in enumerate(tournament.matches):
                print(f"\tRound N°{rnd_number}:")
                TournamentView.print_matches(rnd, "\t\t")
