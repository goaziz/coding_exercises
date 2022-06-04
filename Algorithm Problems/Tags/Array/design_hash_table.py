class MyHashMap:
    def __init__(self):
        self.space_size = 2096
        self.hash_table = [[] for _ in range(self.space_size)]

    def hash_value(self, key):
        hash_key = key % self.space_size
        return hash_key

    def put(self, key: int, value: int) -> None:
        l = self.hash_table[self.hash_value(key)]
        found = False
        for i, j in enumerate(l):
            k, val = j

            if k == key:
                found = True
                break
        if found:
            l[i] = (key, value)
        else:
            l.append((key, value))

    def remove(self, key):
        hash_list = self.hash_table[self.hash_value(key)]
        found = False
        for i, j in enumerate(hash_list):
            k, val = j

            if k == key:
                found = True
                break
        if found:
            del hash_list[i]

    def get(self, key):
        hash_list = self.hash_table[self.hash_value(key)]
        found = False
        for i, j in enumerate(hash_list):
            k, val = j

            if k == key:
                found = True
                break
        if found:
            return val
        else:
            return -1
