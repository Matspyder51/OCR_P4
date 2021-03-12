# from models.player import player
# from models.tournament import tournament
from colorama import init
from controllers import controller

init(autoreset=True)


main = controller.Controller()


# main.home_controller.input_home_menu()
# home.HomeController()

# def createDebugData():
# 	temp_players = [
# 		["Harry", "Potter", "10/04/2000", "H", 0],
# 		["Lionel", "Messi", "10/04/2000", "H", 0],
# 		["Steve", "Jobs", "10/04/2000", "H", 0],
# 		["Bill", "Gates", "10/04/2000", "H", 0],
# 		["Tom", "Jedusor", "10/04/2000", "H", 0],
# 		["Antoine", "Griezmann", "10/04/2000", "H", 0],
# 		["Zinedine", "Zidane", "10/04/2000", "H", 0],
# 		["Barry", "Allen", "10/04/2000", "H", 0]
# 	]

# 	players = []

# 	for ply in temp_players:
# 		players.insert(len(players), player.Player(ply))

# 	print(repr(players[0].__dict__))

# createDebugData()

# ply = player.Player()

# trn = tournament.Tournament()

# trn.add_player(ply)

# print(trn.players)
