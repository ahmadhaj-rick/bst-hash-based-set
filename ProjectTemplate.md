
# Mini-project report 
Members: Ahmad AlHaj Hussain, Ahmad Fahim 
Program: Network Security
Course: 1DV501 or 1DT901  
Date of submission: 2022-11-24

## Introduction  
A simple project implementing Hash Set And Binary search Tree using recursion.
The Porject had three parts
- Part 1 : We used python's set class and dictionary to find count of unique words in a give word list
and produce Top 10 list of words that has lenght larger than 4
- Part 2 : Using the a given skeleton, we implemented Binary search tree and Hash based set.
- Part 3 : We repeated Part 1 but this time using our own DS [Hash set , Binary Search Tree]
1DV501/1DT901.  

## Part 1: Count unique words 1
The text should include:
- We had two different results for each file but they were in close proximity.
- Ahmad Al Haj : ``life_of_brian: 13335 words`` and ``swedish_news_2020: 14133030``
- Ahmad Fahim : ``life_of_brian: 13433 words`` and ``swedish_news_2020: 16360080``

We created a function that takes file name and current path as input then we open the file in read mode
we initiate an empty dictionary, set and list vars.
we use the set class to figure out the unique words since sets dont allow dublicts.

<img src="https://snipboard.io/297OuF.jpg" width="400"/>

While dictionary and list, to find out top ten using thier occurence frequency.
we check for thier lenght, and if we dont have it we add to the dic other wise we increase the frequency.

<img src="https://snipboard.io/N8wu96.jpg" width="400"/>

then simply print the values we have for each file. 

<img src="https://snipboard.io/5seVx3.jpg" width="400"/>

The Results Are shown below:

<img src="https://snipboard.io/tdU47E.jpg" width="400"/>



## Part 2: Implementing data structures
- The BST based map is a linked implementation where each node has four fields (key, value, left-child, right-child).
- The hash-based set is built using a Python list to store the buckets where each bucket is another Python list. 
  The initial bucket list size is 8 and rehashing (double the bucket list size) takes place when the number of elements equals the number of buckets.

- For the hash based word set (HashSet):
- ``get_hash():``
 in this function we take a string as input, then using the ascii value of each char in the string
adding those value toghter will give us a number but to increase the uniquenss of the that hash 
we have a counter that increase by 1 each iteration of char and a magic constant number. 
using those two values we create a number that is constant enought but will make the value of 
``CAT`` AND ``TAC`` wont be the same.

```
# Computes hash value for a word (a string)
    def get_hash(self, word):
        hashh = 0  # hash of a word
        count = 0
        for ch in word:
            count += 1
            # get the ascii value, multiplite by count plus const 600
            # count will increase by len(word), while 600 is a number
            # to increase uniquness.
            hashh += ord(ch) * (count + 600)
        # postion to add in the bucket, using the len of buckets we have as mod
        pos = hashh % len(self.buckets)
        return pos
```

- ``rehash():``

    in the rehash we copy the old buckets into a tmp bucket, then we create new buckets twice the size of the old ones.
    starting buckets init is : [ [] for i in range(8) ], we simple use that in range of the len(old buckets)
    doubling the size : [ [] for i in range(0, len(self.buckts) *2) ] then rest the size to = 0
    after that we starting adding the old elements to the new buckets using the function ``add()`` that will take care of 
    the new size too.
    
    ```
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
    ```

- ``add():``
    the add function takes string as input, try to get a hash by passing the string to get_hash(word)
    after getting the hash we check if we have the word in our buckets by passing it to contains(). 
    if we dont have it, then we check if we have have enough buckets. if we dont we trigger a rehash.
    otherwise we just append the word to our buckets using the hash value as index.

    ```
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

    ```

 * Point out and explain any differences from the given results in ``hash_main.py``
    * the expected output: 
        ```
        to_string(): { Adam David Amer Ceve Owen Ella Jonas Morgan Fredrik Zoe Fred Albin Ola Simon }
        get_size(): 14
        contains(Fred): True
        contains(Bob): False

        max bucket: 2
        bucket list size: 16
        zero bucket ratio: 0.38

        get_size: 10
        to_string(): { David Amer Owen Ella Morgan Fredrik Zoe Fred Albin Simon }
        ```	

    * Our output:
        ```
        to_string(): { David Fred Ella Morgan Zoe Adam Albin Ola Amer Ceve Owen Jonas Fredrik Simon  }
        get_size(): 14
        contains(Fred): True
        contains(Bob): False

        max bucket: 2
        bucket list size: 16
        zero bucket ratio: 0.25

        get_size: 10
        to_string(): { David Fred Ella Morgan Zoe Albin Amer Owen Fredrik Simon  }
        ```
        We can see the order of the to_string and zero_bucket ratio is not the same. And that is because of how the hash 
        function is implemented, getting different values will change the indexing, and effectiveness


- For the BST based map (BstMap), present (and explain in words):
 	* Python code for the two functions ``put`` and ``max_depth``.
 	* Point out and explain any differences from the given results in ``bst_main.py``.

## Part 3: Count unique words 2
- How did you implement the Top-10 part of the problem. Feel free to show code fragments.
- Present a unique word count and the Top-10 lists for each of the two files.
* What is the bucket list size, max bucket size and zero bucket ratio for HashSet, and the total node count, max depth and leaf count for BstMap, after having added all the words in the two large word files? (Hence, eight different numbers.)
* Explain how max bucket size and zero bucket ratio can be used to evaluate the quality of your hash function in HashSet. What are optimal/reasonable/poor values in both cases?
* Explain how max depth and leaf count can be used to evaluate the efficiency of the BstMap. What are optimal/reasonable/poor values in both cases?


## Project conclusions and lessons learned
We separate technical issues from project related issues.
### Technical issues 
- What were the major technical challanges as you see it? What parts were the hardest and most time consuming?
- What lessons have you learned? What should you have done differently if you now were facing a similar problem.
- How could the results be improved if you were given a bit more time to complete the task.

### Project issues
- Describe how your team organized the work. How did you communicate? How often did you communicate?
- For each individual team member: 
 	* Describe which parts (or subtasks) of the project they were responsible for. Consider writing the report as a separate task. Try to identify main contributors and co-contributors.
 	* Estimate hours spend each week (on average)
 - What lessons have you learned? What should you have done differently if you now were facing a similar project.



