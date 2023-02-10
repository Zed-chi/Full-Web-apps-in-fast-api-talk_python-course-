from typing import Optional


class DB:
    def __init__(self):
        self.db = {"users": [], "packages": []}

    def add(self, table, value):
        self.db[table].append(value)

    def update(self, table, pk, key, value):
        for idx, elem in enumerate(self.db[table]):
            if elem["pk"] == pk:
                self.db[table][idx][key] = value

    def delete(self, table: str, pk: str):
        for idx, elem in enumerate(self.db[table]):
            if elem["pk"] == pk:
                del self.db[table][idx]

    def get(self, table: str, pk: str) -> Optional[dict]:
        for elem in self.db[table]:
            if elem["pk"] == pk:
                return elem

    def count(self, table):
        if table not in self.db:
            return
        return len(self.db[table])


db = DB()
