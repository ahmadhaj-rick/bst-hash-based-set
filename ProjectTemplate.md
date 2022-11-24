
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
- 
- How did you implement the Top-10 part of the problem. Feel free to show code fragments.
- Present a unique word count and the Top-10 lists for each of the two files.

In this part we created a function that takes file name and current path as input then we open the file in read mode
we initiate an empty dictionary, set and list vars.
we use the set class to figure out the unique words since sets dont allow dublicts.

<img src="https://snipboard.io/297OuF.jpg" width="400"/>

While dictionary and list, to find out top ten using thier occurence frequency.
we check for thier lenght, and if we dont have it we add to the dic other wise we increase the frequency
<img src="https://snipboard.io/N8wu96.jpg" width="400"/>

then simply print the values we have for each file. 

<img src="https://snipboard.io/5seVx3.jpg" width="400"/>

The Results Are shown below:

<img src="https://snipboard.io/tdU47E.jpg" width="400"/>



## Part 2: Implementing data structures
- Give a brief presentation of the given requirements
- For the hash based word set (HashSet), present (and explain in words):
 	* Python code for function ``add``, how to compute the hash value, and rehashing.
 	* Point out and explain any differences from the given results in ``hash_main.py``
 	
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



