from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word): # this should be done 
        hashh = 0
        for l in word:
            hashh += ord(l)  # get the ascii value and just add it 
        # maybe retrun the hash % the len(buckets) so i dont repeat my self ??
        return hashh  # return the ascii value of the whole word AKA hash


    # Doubles size of bucket list
    def rehash(self):
        for i in range(len(self.buckets)):
            if len(i) > 2 and [for j in range() ]:
                pass # brb 

        pass    # Placeholder code ==> to be replaced

    # Adds a word to set if not already added
    def add(self, word):
        # use the len of the buckets [how many buckets we have] as a mod number.
        mod = len(self.buckets)
        pos = self.get_hash(word) % mod
        self.buckets[pos] # append using the pos 
        # i need to think about the rehashing case here....
        # increase the size every time we add a bucket ?

    # Returns a string representation of the set content
    def to_string(self):
        pass    # Placeholder code ==> to be replaced

    # Returns current number of elements in set
    def get_size(self):
        pass    # Placeholder code ==> to be replaced

    # Returns True if word in set, otherwise False
    def contains(self, word):
        # im repeating code, maybe put it in the hashing func ?
        mod = len(self.buckets)
        pos = self.get_hash(word)
        pass    # Placeholder code ==> to be replaced

    # Returns current size of bucket list
    def bucket_list_size(self):
        pass    # Placeholder code ==> to be replaced

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        pass    # Placeholder code ==> to be replaced

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        pass    # Placeholder code ==> to be replaced

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        pass    # Placeholder code ==> to be replaced
