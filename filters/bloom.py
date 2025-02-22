import mmh3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        """
        Initialize the Bloom filter.
        :param size: Number of bits in the bit array.
        :param hash_count: Number of hash functions to use.
        """
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        """
        Add an item to the Bloom filter.
        :param item: The item (as a string) to be added.
        """
        for i in range(self.hash_count):
            # Generate a hash for the item with different seeds.
            digest = mmh3.hash(item, i) % self.size
            self.bit_array[digest] = True

    def check(self, item):
        """
        Check for the presence of an item in the Bloom filter.
        :param item: The item (as a string) to check.
        :return: False if the item is definitely not in the set,
                 True if the item might be in the set.
        """
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if not self.bit_array[digest]:
                return False
        return True