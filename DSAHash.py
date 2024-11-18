import numpy as np
from DSALinkedlist import DSALinkedList
from DSAHeap import DSAHeap

class DSAHashEntry:
    def __init__(self, key="", value=None, state=0):
        self.key = key
        self.value = value
        self.state = state
    
    def getKey(self):
        return self.key

class DSAHashTable(DSAHeap):
    resizer = 0
    def __init__(self, max_size, initial_size = 10, loadFactorThreshold=0.7, shrinkFactorThreshold=0.3):
        super().__init__(max_size)
        self.table_size = self.next_prime(initial_size)
        self.shopHashTable = np.empty(self.table_size, dtype=object)
        self.count = 0
        self.loadFactorThreshold = loadFactorThreshold
        self.shrinkFactorThreshold = shrinkFactorThreshold
        self.hashShops = DSALinkedList()

    def print_table_size(self):
        print("Hash table size:", self.table_size)

    def get_shops_in_category(self, category):
        try:
            hashIdx = self.hash(category.lower())
            category = category.lower()
            found = False

            for entry in self.shopHashTable:
                if entry is not None and entry.state == 1:
                    found = True
                    entry_category = entry.key.lower()
                    if self.hash(entry.key.lower()) == hashIdx and entry_category == category:
                        rating = entry.value.rating
                        self.addShop_to_heap(rating, entry)
            if not found:
                print(f"No shops found in the category '{category}'.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def display_hash_table(self, category):
        try:
            hashIdx = self.hash(category.lower())
            category = category.lower()
            found = False

            for entry in self.shopHashTable:
                if entry is not None and entry.state == 1:
                    found = True
                    entry_category = entry.key.lower()
                    if self.hash(entry.key.lower()) == hashIdx and entry_category == category:
                        print("Shop Category : ", entry.getKey(), 
                                "\tShop Number : ", entry.value.shop_number,
                                '\tShop Name : ', entry.value.shop_name,
                                '\tLocation : ', entry.value.location,
                                '\tRating : ', entry.value.rating)

            if not found:
                print(f"No shops found in the category '{category}'.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def put(self, inKey, inValue): 
        try:
            hashIdx = self.hash(inKey.lower())
            origIdx = hashIdx

            while self.shopHashTable[hashIdx] is not None and self.shopHashTable[hashIdx].state == 1:
                hashIdx = (hashIdx + 1) % len(self.shopHashTable)
                if hashIdx == origIdx:
                    self.resize(self.next_prime(self.table_size * 2))

            self.shopHashTable[hashIdx] = DSAHashEntry(inKey, inValue, 1)
            

            if hashIdx > self.resizer:
                self.resizer = hashIdx

            # Check the load factor and resize if needed
            load_factor = self.count / self.table_size
            if load_factor > self.loadFactorThreshold:
                self.resize(self.next_prime(self.table_size * 2))
                print("Load factor exceeded resizing the array.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def remove_shop_from_hash(self, shop_number, category):
        try:
            hashIdx = self.hash(category.lower()) 
            origIdx = hashIdx
            found = False

            while not found:
                entry = self.shopHashTable[hashIdx]
                if entry is not None and entry.state == 1:
                    if entry.key == category and entry.value.shop_number == shop_number:
                        found = True
                        entry.state = 0  # Mark the entry as removed
                        entry.key = None
                        self.count -= 1  # Decrement the count
                        print(f"\nShop with shop number {shop_number} in category '{category}' removed from shop hash table\n")
                    else:
                        hashIdx = (hashIdx + 1) % len(self.shopHashTable)
                        if hashIdx == origIdx:
                            break

            # Check the load factor and resize if needed
            load_factor = self.count / self.table_size
            if load_factor < self.shrinkFactorThreshold:
                new_size = max(self.next_prime(self.table_size // 2), self.resizer + 1)
                self.table_size = new_size
                self.resize(new_size)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def resize(self, new_size):
        try:
            # check that the new size is greater than or equal to the current count
            new_size = max(new_size, self.count)
            self.table_size = new_size

            # Create a new hash array with the new size
            new_array = np.empty(new_size, dtype=object)

            # Rehash and insert existing entries into the new array
            for entry in self.shopHashTable:
                if entry is not None and entry.state == 1:
                    self._rehash_and_insert(new_array, entry)

            self.table_size = new_size
            self.shopHashTable = new_array
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def _rehash_and_insert(self, new_array, entry):
        try:
            
            hashIdx = self.hash(entry.key.lower())
            origIdx = hashIdx

            while new_array[hashIdx] is not None:
                hashIdx = (hashIdx + 1) % len(new_array)
                if hashIdx == origIdx:
                    raise Exception("\nNew array is full")

            new_array[hashIdx] = entry
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def hash(self, key):
        try:
            hashIndex = 0
            for char in key.lower():
                hashIndex += ord(char)
            return hashIndex % self.table_size
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def next_prime(self, num):
        try:
            while not self.is_prime(num):
                num += 1
            return num
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def is_prime(self, num):
        try:
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True
        except Exception as e:
            print(f"An error occurred: {str(e)}")