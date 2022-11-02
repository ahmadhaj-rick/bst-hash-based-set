from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        # this is basically number of elements best case is 1 word = 1 bucket
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        hashh = 0  # hash of a word
        for l in word:
            hashh += ord(l)  # get the ascii value and just add it
        # postion to add in the bucket, using the len of buckets we have as mod
        pos = hashh % len(self.buckets)
        return pos

    # Doubles size of bucket list
    def rehash(self):
        origin_buckt = self.buckets  # make a copy of the original buckts

        # double the size of the buckts [len(buckts) * 2]
        # we can take the same formula as init buckts
        # [[] for i in range(8)] -> [[] for i in range(0, len(self.buckts) *2)]
        # copy old buckts to the new one.
        # reset the size since its new buckets

        self.size = 0
        self.buckets = [[] for i in range(0, len(self.buckets) * 2)]

        # copy the old to the new
        for i in origin_buckt:  # point to each buckt in buckts
            for words in i:  # point the word inside buckt from buckts
                self.add(words)  # send the word to the add

    # Adds a word to set if not already added
    def add(self, word):
        pos = self.get_hash(word)  # pos
        # check if the word is already in a bucket
        if self.contains(word) is False:
            # check if we maxed our buckets.
            if self.size == len(self.buckets):
                self.rehash()  # rehash [double the size, copy old to new]
                self.add(word)  # try to add the word again.
            # we didnt max ? then just add the word.
            else:  # self.size != len(self.buckets)
                self.buckets[pos].append(word)  # add the word
                self.size += 1  # increase our size counter

    # Returns a string representation of the set content
    def to_string(self):
        this_string = "{ "
        for bucket in self.buckets:  # point to each bucket
            for word in bucket:  # point to the word inside a bucket
                # add the word to this_string
                this_string += word + " "
        this_string += " }"  # close the string with }
        return this_string  # send the results

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        pos = self.get_hash(word)  # get the pos from the hash()
        if word in self.buckets[pos]:  # check if its in the buckets
            return True
        else:
            return False

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        if self.contains(word) is True:
            pos = self.get_hash(word)
            self.buckets[pos].remove(word)
            self.size -= 1

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        # this is the oppesit of the zero buckets.
        # see each len(self.buckets[i]) and store and compare with the next
        # until we have final biggest len(self.buckets[i])
        # i'll be back here
        bucket_size = 0

        for i in range(len(self.buckets)):
            if len(self.buckets[i]) > bucket_size:
                bucket_size = len(self.buckets[i])

        return bucket_size

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        # if len(self.buckets[i]) == 0 this is an unused bucket
        # we count each time we hit a zero buckets then see our overall size
        # divid the zero-buckets // len(self.buckets)
        # i'll be back here
        empty_buckets = 0
        for i in range(len(self.buckets)):
            if len(self.buckets[i]) == 0:
                empty_buckets += 1
        ratio = empty_buckets / len(self.buckets)
        return ratio
