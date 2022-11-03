import BstMap as bst
import HashSet as hsh
from operator import itemgetter


# defining some functions to use our Data structer
def create_bst(words):
    the_tree = bst.BstMap()  # create and init the tree
    for word in words:
        # if we dont have it, it will be none
        # if we do have it, we used check as the value param.
        check = the_tree.get(word)
        if check is None:
            the_tree.put(word, 1)
        else:
            the_tree.put(word,  check + 1)
    return the_tree


def create_hash_set(words):
    the_set = hsh.HashSet()  # create the hash set
    the_set.init()  # init the hash set
    for word in words:
        the_set.add(word)
    return the_set


# read the file and save it to a var
def opening_files(file_name):
    with open(file_name, "r", encoding="UTF-8") as file:
        data = file.read().lower().split("\n")
    return data


def top_ten(lst):
    iteams, counter = "", 0
    for x in lst:
        # we have the break check here to avoid an extra result
        if counter == 10:
            break
        elif len(x[0]) > 4:  # checks if the key is bigger than 4 char
            counter += 1
            iteams += f"{x[0]}, {x[1]}\n"
    return iteams


"""
1-Count how many unique words that are used in the two given texts
files using your HashSet implementation.

2-Present a list of the top-10 most frequently used words
having a length larger than 4 using your BstMap implementation.

3-What is the:
a) bucket list size, b) max bucket size, and
c) zero bucket ratio for the HashSet after having added
all words in the two large text files Life of Brian
and News items respectively?

4-What is the a) number of tree nodes, b) max depth, and
c) leaf count of the BST when adding all words (as both key and value)
from the large text files (Life of Brian and News items respectively)?
"""
brain = opening_files("brain_13335_words.txt")
swe_news = opening_files("swe_14133030_news")

# brain hash set OP
brain_hssh = create_hash_set(brain)
print("Life of Brain Hash Set")
print(f"Bucket list size: {brain_hssh.bucket_list_size()}")
print(f"Max bucket size: {brain_hssh.max_bucket_size()}")
print(f"Zero bucket ratio: {round(brain_hssh.zero_bucket_ratio(), 2)}")
print()

# brain bst OP
brain_tree = create_bst(brain)
print("Life of Brain Binary Search Tree")

print(f"Number of tree nodes: {brain_tree.size()}")
print(f"Max depth: {brain_tree.max_depth()}")
print(f"Leaf count: {brain_tree.count_leafs()}")
print()

# swedish news hash set OP
swe_hash = create_hash_set(swe_news)
print("Swedish News Hash Set")

print(f"Bucket list size: {swe_hash.bucket_list_size()}")
print(f"Max bucket size: {swe_hash.max_bucket_size()}")
print(f"Zero bucket ratio: {round(swe_hash.zero_bucket_ratio(), 2)}")
print()

# swedish news bst OP
swe_tree = create_bst(swe_news)
print("Swedish News Binary Search Tree")

print(f"Number of tree nodes: {swe_tree.size()}")
print(f"Max depth: {swe_tree.max_depth()}")
print(f"Leaf count: {swe_tree.count_leafs()}")
print()

# Top ten section

# save the list to a var to do some stuff to it [sort]
swe_lst = swe_tree.as_list()

# sort the list using the value [1], while keys[0].
# going higest to lowest using the reverse=True
sort_swe_lst = sorted(swe_lst, key=itemgetter(1), reverse=True)

# save the list to a var to do some stuff to it [sort]
brain_lst = brain_tree.as_list()

# sort the list using the value [1], while keys[0].
# going higest to lowest using the reverse=True
sort_brain_lst = sorted(brain_lst, key=itemgetter(1), reverse=True)

# Printing Top Ten
print(f"Top Ten for brain: {top_ten(sort_brain_lst)}")
print(f"Top ten for swedish news: {top_ten(sort_swe_lst)}")
