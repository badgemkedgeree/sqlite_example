
class Game:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def save(self, cursor):
        cursor.execute(f'INSERT INTO games (name, rank) VALUES ("{self.name}",{self.rank})')
