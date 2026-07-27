class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hash_value = self.hash(key)

        # If this hash doesn't exist yet, create a new nested dictionary
        if hash_value not in self.collection:
            self.collection[hash_value] = {}

        # Store the key-value pair in the nested dictionary
        self.collection[hash_value][key] = value

        print(f"Added key: {key}, value: {value}, hash: {hash_value}")

    def remove(self, key):
        hash_value = self.hash(key)

        #check if hash_value is in collection and key in hash_value.collection then delete
        if hash_value in self.collection and key in self.collection[hash_value]:
            del self.collection[hash_value][key]

            # if hash_value not in collection delete
            if not self.collection[hash_value]:
                del self.collection[hash_value]

    def lookup(self, key):
        hash_value = self.hash(key)

        #return hash_value and key
        if hash_value in self.collection and key in self.collection[hash_value]:
            return self.collection[hash_value][key]
        else:
            return None


# Example
table = HashTable()

table.add("Alice", 95)
table.add("Bob", 87)
table.add("Alex", 88)

print(table.collection)
