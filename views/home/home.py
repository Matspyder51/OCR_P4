from colorama import Fore


class HomeView:

    @staticmethod
    def print_start_message():
        print(f"Welcome in {Fore.GREEN}ChessTournamentManager {Fore.YELLOW}version 0.0.1")

    @staticmethod
    def print_home_menu():
        print("Type \"quit\" to exit the program")
        print("Home menu :")
        print(f"{Fore.RED}[1] {Fore.RESET}Create a new tournament")
        print(f"{Fore.RED}[2] {Fore.RESET}Manage Players")
        print(f"{Fore.RED}[3] {Fore.RESET}Load a tournament")
        print(f"{Fore.RED}[4] {Fore.RESET}View tournament overwiew")

    @staticmethod
    def print_home_menu_selection_error(error: str):
        print(f"{Fore.RED}Your entry is incorrect: {error}")
