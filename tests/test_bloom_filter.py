import pytest
import random
import string
from filters.bloom import BloomFilter

@pytest.fixture
def bf():
    """
    Fixture to create a BloomFilter instance.

    Returns:
        BloomFilter: An instance of BloomFilter with 10,000 bits and 7 hash functions.
    """
    return BloomFilter(10000, 7)

def test_add_and_check(bf):
    """Test adding a single element to the Bloom filter and checking its membership.

    This test asserts that:
      - An element that is added is detected in the filter.
      - An element that is not added is not detected.

    Args:
        bf (BloomFilter): Instance of BloomFilter class injected
    """
    bf.add("test_element")
    assert bf.check("test_element") is True, "Element found in Bloom filter."
    assert bf.check("nonexistent") is False, "Element NOT found in Bloom Filter."

def test_multiple_elements(bf):
    """Test adding multiple elements to the Bloom filter.

    This test adds several known elements and asserts that each is found in the filter.
    It also checks that an element that was not added is (most likely) not found.

    Args:
        bf (BloomFilter): Instance of BloomFilter class injected
    """
    elements = ["apple", "banana", "cherry", "date", "elderberry"]
    for element in elements:
        bf.add(element)
    for element in elements:
        assert bf.check(element) is True, "Elemens found in the Bloom filter"
    assert bf.check("fig") is False, "Element NOT found in the Bloom filter"

def test_false_positive_rate(bf):
    """Test the false positive rate of the Bloom filter.

    Inserts a number of random strings into the Bloom filter, then tests a set of new random
    strings to estimate the false positive rate. Asserts that the false positive rate is below
    an acceptable threshold (10%).

    Args:
        bf (BloomFilter): Instance of BloomFilter class injected
    """

    inserted = set()
    num_elements = 1000
    # Insert random strings into the Bloom filter.
    for _ in range(num_elements):
        word = ''.join(random.choices(string.ascii_lowercase, k=8))
        inserted.add(word)
        bf.add(word)
    
    false_positive_count = 0
    test_runs = 1000
    # Test with new random strings and count false positives.
    for _ in range(test_runs):
        word = ''.join(random.choices(string.ascii_lowercase, k=8))
        if word not in inserted and bf.check(word):
            false_positive_count += 1

    false_positive_rate = false_positive_count / test_runs

    assert false_positive_rate < 0.1, "False positive rate is above 10%."
