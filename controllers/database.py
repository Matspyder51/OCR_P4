from tinydb import TinyDB


def get_database():
    return TinyDB("database.json", indent=4)


def get_table(name: str):
    return get_database().table(name)
