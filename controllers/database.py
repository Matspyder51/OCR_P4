from tinydb import TinyDB


def get_database():
    """Return database TinyDB Object"""
    return TinyDB("database.json", indent=4)


def get_table(name: str):
    """Return the TinyDB table"""
    return get_database().table(name)
