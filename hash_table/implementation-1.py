
class HashTable:

    def __init__(self, limit):
        self.hash_table = [[], ] * limit

    @staticmethod
    def check_prime(n):
        if n == 1 or n == 0:
            return 0

        for i in range(2, n // 2):
            if n % i == 0:
                return 0
        return 1

    def get_prime(self, n):
        if n % 2 == 0:
            n += 1
        while not self.check_prime(n):
            n += 2
        return n

    def hash_function(self, key):
        capacity = self.get_prime(10)
        return hash(key) % capacity

    def insert_data(self, key, data):
        index = self.hash_function(key)
        self.hash_table[index] = [key, data]

    def remove_data(self, key):
        index = self.hash_function(key)
        self.hash_table[index] = 0


has_map = HashTable(limit=20)
print(len(has_map.hash_table))
for i in range(20+1):
    has_map.insert_data(key=str(i), data=1)
print(has_map.hash_table)
