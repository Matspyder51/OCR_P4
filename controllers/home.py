from views.home import home


class HomeController:

    _view: home.HomeView

    def __init__(self):
        self._view = home.HomeView()
        self._view.print_start_message()

    def input_home_menu(self):
        self._view.print_home_menu()
        entry = input("Please enter the number of the menu you want to select : ")
        if entry == "quit":
            return

        try:
            converted = int(entry)
            return converted
        except ValueError:
            self._view.print_home_menu_selection_error("Please enter a valid number")
            return self.input_home_menu()
