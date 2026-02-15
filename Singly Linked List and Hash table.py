# Node class for linked list
class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


# Hash Table class
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Insert key-value pair
    def put(self, k, v):
        idx = hash(k) % self.size
        self.table[idx] = Node(k, v, self.table[idx])

    # Search value using key
    def get(self, k):
        idx = hash(k) % self.size
        curr = self.table[idx]

        while curr:
            if curr.key == k:
                return curr.val
            curr = curr.next

        return None


# Driver code
ht = HashTable(5)

ht.put("ID_1", "Alice")
ht.put("ID_2", "Bob")

print(ht.get("ID_1"))
print(ht.get("ID_2"))
print(ht.get("ID_3"))   # Not present
