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


- For the BST based map (BstMap):

``put():``
    this function, takes key, and value as input.
    we use gaurd statment at the start of the fucntion since we going to be call it recursivly. 
    
    1- check if the input key is the same as the key we checking against.

    2- else we check if its less so we can go left which will take use to see if there is no left node if true we create a node with the inputted key, value otherwise we go to the else.
    
    3- the else is a recursive call to the method it self on the left node of the current node we are at.
    that will repeate steps 1 to 3.
    
    but if step 2 fails then we go to else that will handle it as right side move. which will do steps 1 and 2,
    until one of the calls ethier ends at creating a new node or updating a node at that point the call will exit.
        ```
            def put(self, key, value):
        if key == self.key:  # to replace the values
            self.value = value
        elif key < self.key:  # we going left side
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.left.put(key, value)
        else:  # we going right side
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right.put(key, value)
        ```

``max_depth()``
this function takes the root node as starting point, we have two vars that register the count of each node while digging down the tree recursivly, we go left until we hit a None, then we head right until we reach the bottom or a leaf that has no left AND right. then we count up the recursive call while keeping score of left and right itirations. after each big exit of recursive call we compare left and right we decide who to increment by check if left_side is bigger than right after each recursive call.

```
def max_depth(self):
        left_side = 0
        right_side = 0
        # reach the bottom
        if self.left is not None:
            left_side = self.left.max_depth()
        if self.right is not None:
            right_side = self.right.max_depth()

        # count going up the recursive call
        if left_side > right_side:
            return left_side + 1
        else:
            return right_side + 1
```
Point out and explain any differences from the given results in ``bst_main.py``.

There is no differences from the expected output and our output.

## Part 3: Count unique words 2
- implementting the Top-10:

    We created a function that takes a list of key value pairs as input.
    1- we have a gaurd if statment that checks if our counter has counted 10 iteams.
    
    2- elif we check if the 0 index value [which is the key] has a len bigger than 4, if True we increamnet our counter and loop again until we have all keys of lenght bigger than 4 in a list. 
    ```
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
    ```

    3- then we sort the list by its value value in reverse order which means highest to lowest. And Print our findings.
    ```
    # sort the list using the value [1], while keys[0].
    # going higest to lowest using the reverse=True
    sort_swe_lst = sorted(swe_lst, key=itemgetter(1), reverse=True)
    ```

- The unique word count for both file are same as Part1 result:
    ``Life Of Brain:``

        ```
        Top Ten for brain: 
        brian, 366
        crowd, 161
        centurion, 121
        mother, 103
        right, 100
        crucifixion, 78
        pilate, 68
        pontius, 64
        rogers, 52
        there, 44
        ```
    ``Swedish News: ``
    
        ```
        Top ten for swedish news: 
        säger, 47512
        under, 45081
        kommer, 42247
        efter, 36582
        eller, 30851
        också, 30113
        andra, 27176
        finns, 26967
        sedan, 24909
        skulle, 23530
        ```

* HashSet results for both files:
    - Life of brain:
        ```
        Size of the buckets: 2028
        Bucket list size: 2048
        Max bucket size: 6
        Zero bucket ratio: 0.38
        ```
    - Swedish News: 
        ```
        Size of the buckets: 362946
        Bucket list size: 524288
        Max bucket size: 18
        Zero bucket ratio: 0.6
        ```
* Bst Map results for both files:
    - Life of brain:
        ```
        Number of tree nodes: 2028
        Max depth: 27
        Leaf count: 656
        ```
    - Swedish News: 
        ```
        Number of tree nodes: 362946
        Max depth: 46
        Leaf count: 119482
        ```
* How max bucket size and zero bucket ratio can be used to evaluate the quality of the hash function in HashSet?

    Those two numbers can show use the number of unused buckets hence our unique hash production that will determine the distrubation of the iteams across the buckets. in contrast max bucket size will show how many buckets we have that will conribute to the space size on disk of our operation. 
    taking those two factors intp account, optimizing our hash fucntion can help, reduce space size and operation time.

* how max depth and leaf count can be used to evaluate the efficiency of the BstMap?

    Those two values will show how balanced our tree is if one side is deeper than the other or if we have too many lone nodes [leafs], in perfect word we would want a perfeclty balanced tree of equal wieghts on both sides left and right.


## Project conclusions and lessons learned
We separate technical issues from project related issues.
### Technical issues 
- What were the major technical challanges as you see it? What parts were the hardest and most time consuming?

    The project was fun to work on, we would say the hardest was:
    1- Understanding recursive functions and how they work.
    2- coming up with a unique enough hash function, took alot of expermenting.


- What lessons have you learned? What should you have done differently if you now were facing a similar problem.

    1- Always have a paper and pen right beside, writing things and drawing them, helps in understanding the problem you trying to solve.
    2- break down problems into smaller problems and solve bite size.
    3- nothing wrong with spending half the time researching and looking up concepts online. Afterall you can't use a tool you dont fully understand.
    [Dont Shoot your self in the leg]
- How could the results be improved if you were given a bit more time to complete the task.

    We'd work more on the Hash fucntiong, try to make it a uniqe as possible but its a broad subject and field that requires alot of advanced math.
    
    try to fiter and organize the word list more, to squeeze as much as possible data. 

### Project issues

We meet up 3 times a week, and used Whatsapp/TeamViewer when ever possible
we compared notes, and exchanged ideas. How to make the progam more coherent and compatable.

``Main-contributor Ahmad Al Haj``  
I worked on Part 2 and 3, while discussing and reflecting ideas with my partner, we reached a working solution. 
I have advanced my skills using recursive functions, and with in hashing from a practical script-kiddie levelish to a real understanding which makes me want to revist HashCat toolset. so it was refreshing.

i spent around 15 to 20 hours a week mainly with my partner.

i'd plot out the idea on paper on pen, breaking it down to smaller sets of problems then approach it.
    
``Co-contributor Ahmad Fahim:``
    While it is safe to say that we our teamwork has been synergistic and substantive, there still have been some predicaments on the account of a lopsided skill parity between myself and my partner (aa226un). While my partner had a more solid foothold in the field thanks to the countless years of experience and endeavor, relatively I am a novice who is yet to master more in-depth knowledge and insight into the fundamentals of the programming. Nevertheless, the experience from this collaboration has been both productive and informative as it has helped me improve my rudimentary knowledge of the subject. Moreover, I have diligently worked and proactively participated in every phase of this project with my partner to ensure that I contribute to the work and subsequently get a more a coherent project result. While my fundamental focus has been the part one, which consumed a reasonable number of rigorous hours every day, I also strove to contribute to the remaining two of parts of the project.  Furthermore, my partner has been very accommodating with giving me an ample room for contribution in the other parts of project that he has endeavored to complete. Given that the task in whole has been difficult and arduous, I was compelled to spend an average 40 hours a week researching, applying and formulating the program using all available resources and wherewithal at my disposal. It is noteworthy to highlight that my partner aa226un and I communicated regularly on the campus as well as using the online means such as TeamViewer and WhatsApp with the goal of exchanging ideas and information to improve the codes as well as integrating the different parts into a more coherent program. Therefore, the task has undergone some major and minor overhauls along the way.

In my belief, the overarching result of our joint project has been reasonably successful notwithstanding the wide margin in the skill parity,  that afforded my partner aa226un an enviable edge. I have gained a substantial insight into the project and more radical improvements in my case are warranted and it behooves me to expend more time and endeavor to acquire the programming acumen and make the playing field more even in the future joint tasks. In hindsight, I should have participated more in the tutoring sessions as they presented ample opportunity to garner the much-needed support from the teaching assistants. Had I maintained a more proactive presence in the tutoring sessions, I would have saved more time on the project and my task would not have required frequent tampering and problems could have been solved much earlier.

Moreover, in retrospect, I should have expended more time in immersive research about the Binary tree and hashing as they make up the core components of the project, and garnering more experience in them, gives me a considerable parity with the future teammates. Should I face the same task again, I would use a different modus operandi which would require putting other classes on secondary priority list and use all available time and energy into a research, practice, experimenting and simulating with the smaller tasks in advance, as to gradually prepare for solving more complex problems in the actual project. Going directly into the project with the prerequisite preparatory tools can get elusive, therefore, I must recalibrate my approach to the task by immersing and harnessing the logical order of these kinds of programs. 
My main fouces was part one, but we collabrated and discussed two and three, since there is a big skill gap. i have learned alot on the way and as a team we got the work done. Hopefully on the next project we will level the playinig field.

