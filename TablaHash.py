class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def contains(self, key):
        return key in self.table

    def remove(self, key):
        if key in self.table:
            del self.table[key]

    def get(self, key):
        return self.table.get(key)