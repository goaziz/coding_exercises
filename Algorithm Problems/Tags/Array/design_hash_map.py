class MyList:
    def __init__(self):
        self.new_list = []

    def put(self, key, value):
        found = False
        for i, j in enumerate(self.new_list):
            if key == j:
                self.new_list[i] = value
                found = True
                break
        if not found:
            self.new_list.append(value)

    def get(self, key):
        for i in self.new_list:
            if i == key:
                return i
        return -1

    def remove(self, key):
        for i, j in enumerate(self.new_list):
            if key == j:
                del self.new_list[i]


class MyHashMap:
    def __init__(self):
        self.space_size = 2096
        self.hash_table = [MyList() for _ in range(self.space_size)]

    def hash_value(self, key):
        hash_key = key % self.space_size
        return hash_key

    def put(self, key: int, value: int) -> None:
        self.hash_table[self.hash_value(key)].put(key, value)

    def remove(self, key: int) -> None:
        self.hash_table[self.hash_value(key)].remove(key)

    def get(self, key: int) -> bool:
        return self.hash_table[self.hash_value(key)].get(key)
