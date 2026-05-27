# Implementing hash table
class HashTable:
    # Constructor method for hash table
    def __init__(self, size = 7):
        self.data_map = [None] * size

    # Hash method
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    # Method to print table
    def print_table(self):
        for i, num in enumerate(self.data_map):
            print(f"{i} : {num}")

    # Method to set the items in our hash table
    def set_items(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    # Method to get the items from hash table
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    # Method to get all the keys from our hash table
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


# Interview question items in common
def items_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for i in list2:
        if i in my_dict:
            return True
    return False
