class SimpleHashMap:
    """Simple Implementation of a HashMap"""
    
    def __init__(self):
        """Constructor for the Hash Map. Initiates an empty array with 20 slots"""
        self._items = [[] for _ in range(20)]
    
    def hash_key(self, key):
        """Hash method to store the key
            This function sums the character code for each character in the key
            use this number to store data in array index

            RunTime: O(n) -  not great
        """
        hashed_key = sum((ord(char) for char in key))
        return hashed_key % 20
    
    def set_new(self, new_key, new_value):
        """
            Appends a new key/value pair to the array.

            HashTable Runtime: O(1) - Implementation:
            self._items.append([new_key, new_value])
            return [new_key, new_value]

            HashTable Runtime: O(1)
        """
        hashed_key = self.hash_key(new_key) 

        self._items.insert(hashed_key, new_value)
        
        return self.get_items()


    def get(self, search):
        """
            Uses search as the key and returns the value.
            HashTable Runtime: O(n)
            value = None

            for key, val in self._items:
                if search == key:
                    value = val

            RunTime: O(1) - however, it's important to note that hash func is O(n) so it's not great.
        """
        hashed = self.hash_key(search)
        return self._items[hashed]

    def get_keys(self) -> list:
        """
            Loops through the array and returns the keys.
            HashTable Runtime: O(n)
        """
        keys = []
        for key, value in self._items:
            keys.append(key)
        return keys
  
    def get_values(self) -> list:
        """
            Loops through the array and returns the keys.
            HashTable Runtime: O(n)
        """
        values = []
        for key, value in self._items:
            values.append(value)
        return values
    
    def get_items(self) -> list:
        """
            Returns all items in hash table
            HashTable Runtime: O(1)
        """
        return self._items

    def has(self, key) -> bool:
        """
            Checks to see if key exists within array and returns True or False
            HashTable Runtime: O(n)
                Notes: While "has" is O(n) the function called "get" is O(n).
        """
        if self.get(key) is not None:
            return True
        return False