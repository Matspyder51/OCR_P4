from views.tournament import tournament
from models import player, tournament as tournament_model
from models.match import Match
from utils import to_boolean, ask_data
import datetime


class TournamentController:

    _view: tournament.TournamentView
    _tournament: tournament_model.Tournament

    @property
    def players(self):
        return self._tournament.players

    def __init__(self):
        self._view = tournament.TournamentView()

    def start_new_tournament(self):
        self._tournament = tournament_model.Tournament()

    def add_player(self, ply: player.Player, is_new: bool = False):
        self._tournament.add_player(ply)

        if is_new:
            ply.add_player_in_json()

        self._view.print_player_added(f"{ply.lastname} {ply.firstname}")

    def add_players_in_tournament(self):
        while len(self.players) != 2:
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
                rank = int(input("Please enter the rank of the player : "))

                self.add_player(
                    player.Player([lastname, firstname, birthdate, sex, rank]),
                    is_new_player,
                )
            else:
                search = input("Please enter player's name to find : ")
                possible_players = player.Player.get_player_from_name(search)
                if len(possible_players) < 1:
                    self._view.print_error("No player founded")
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
                        ],
                        final.doc_id
                    ),
                    is_new_player,
                )

    def create_new_tournament(self):
        self._tournament = tournament_model.Tournament()
        self._tournament.name = input("Please enter tournament name : ")
        self._tournament.place = input("Please enter the place of the tournament : ")
        self._tournament.date = input("Please enter the date of the tournament : ")
        self._tournament.round_amount = int(input("Please enter the amount of rounds for this tournament: "))

        self.add_players_in_tournament()

        self._tournament.save_tournament()

        self.generate_matches(True)

    def __get_next_opponent_for_player(self, ply, players):
        opponent: player.Player

        for user in players:
            m = Match(ply, user)
            hasPlayed = False
            for rnd in self._tournament.matches:
                for match in rnd:
                    if match == m:
                        hasPlayed = True
                        break
            if not hasPlayed:
                opponent = user
                break

        return opponent

    def generate_matches(self, first_round: bool = False):
        self._tournament.current_round += 1
        self._tournament.matches.append([])
        matches = []
        if first_round:
            _temp_players = self._tournament.players.copy()
            _temp_players.sort(key=lambda x: x.rank, reverse=True)
            upper = []
            lower = []

            for i in range(len(_temp_players)):
                if i < (len(_temp_players) - 1) / 2:
                    upper.insert(len(upper), _temp_players[i])
                else:
                    lower.insert(len(lower), _temp_players[i])

            for i in range(len(upper)):
                match = Match()
                match.upPlayer = upper[i]
                match.downPlayer = lower[i]
                matches.insert(len(matches), match)

        else:
            _temp_players = self._tournament.players.copy()
            _temp_players.sort(key=lambda x: (x.tournament_rank, x.rank), reverse=True)

            while len(_temp_players) > 0:
                current = _temp_players[0]
                _temp_players.remove(current)
                opponent = self.__get_next_opponent_for_player(current, _temp_players)

                matches.insert(len(matches), Match(current, opponent))

                _temp_players.remove(opponent)

        self._tournament.matches[self._tournament.current_round] = matches
        self._tournament.save_tournament()
        self._view.print_matches_list(matches, self._tournament.current_round)

        self.enter_match_result()

    def __load_tournament(self, data, start: bool = False):
        self._tournament = tournament_model.Tournament()
        self._tournament.load_from_database(data)

        if start and not self._tournament.ended:

            if len(self._tournament.matches) >= self._tournament.round_amount and self._tournament.is_all_matches_of_round_ended():
                self._tournament.ended = True
                self._tournament.save_tournament()
                self._view.print_tournament_overview(self._tournament)
                return

            if self._tournament.is_all_matches_of_round_ended():
                if self._tournament.current_round == -1:
                    self.generate_matches(True)
                else:
                    self.generate_matches()
            else:
                self._view.print_matches_list(self._tournament.matches[self._tournament.current_round], self._tournament.current_round)
                self.enter_match_result()

    def list_tournaments(self):
        tournaments = tournament_model.Tournament.get_tournaments()

        self._view.print_tournaments_list(tournaments)

        selected = int(input("Please enter the id of the tournament to load: "))
        final = next(x for x in tournaments if x.doc_id == selected)
        self.__load_tournament(final)

    def list_all_tournaments(self):
        tournaments = tournament_model.Tournament.get_all_tournaments()
        self._view.print_tournaments_list(tournaments)

        selected = int(input("Please enter the id of the tournament to load: "))
        final = next(x for x in tournaments if x.doc_id == selected)
        self.__load_tournament(final, False)

        self._view.print_tournament_overview(self._tournament)

    def enter_match_result(self):
        matchId = int(input("Please enter the id of the match : "))
        match = self._tournament.matches[self._tournament.current_round][matchId]
        if match.ended:
            return self.enter_match_result()
        winner = int(input("Please enter 0 or 1 to define the winner, enter 3 if the result is a draw : "))
        match.winnedBy = winner
        if winner == 0:
            match.upPlayer.tournament_rank += 1
        elif winner == 1:
            match.downPlayer.tournament_rank += 1
        else:
            match.upPlayer.tournament_rank += .5
            match.downPlayer.tournament_rank += .5
        match.ended = True
        match.endTime = datetime.datetime.now().timestamp()

        self._tournament.save_tournament()

        if not self._tournament.is_all_matches_of_round_ended():
            self._view.print_matches_list(self._tournament.matches[self._tournament.current_round], self._tournament.current_round)
            self.enter_match_result()
        else:
            if self._tournament.round_amount - 1 <= self._tournament.current_round:
                self._view.print_tournament_overview(self._tournament)
                self._tournament.ended = True
                self._tournament.save_tournament()
            else:
                self.generate_matches()