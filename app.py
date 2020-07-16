class MyHashMap:
    """Simple Implementation of a HashMap"""
    
    def __init__(self):
        """Constructor for the Hash Map. Initiates an empty array"""
        self._items = []
    
    def set_new(self, new_key, new_value):
        self._items.append([new_key, new_value])
        return [new_key, new_value]

    def get(self, search):
        value = None

        for key, val in self._items:
            if search == key:
                value = val
        return value

    def has(self, search) -> bool:
        if self.get(search) is not None:
            return True
        return False

    