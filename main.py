from filters.bloom import BloomFilter

if __name__ == '__main__':
    # Create a Bloom filter with 500,000 bits and 7 hash functions.
    bf = BloomFilter(500000, 7)
    
    # Add items
    bf.add("hello")
    bf.add("world")

    # Check for items
    test_items = ["hello", "world", "python"]
    for item in test_items:
        if bf.check(item):
            print(f"'{item}' is possibly in the Bloom filter.")
        else:
            print(f"'{item}' is definitely not in the Bloom filter.")
