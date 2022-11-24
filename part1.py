import os
# intends to store the current working directory route to the variable supreme_route.
supreme_route = os.getcwd()
# We store the targeted files into the variables
Brain_file = 'life_of_13433_brian.txt'
Swedish_file = 'swe_16360080_news.txt'
# Function intends to return the 2nd value,
#while indexing 1 value from the list tpl
def get_value(tpl): 
    return tpl[1]
def count_the_all_un_words(user_input, supreme_route):
# Intends to open the file user_input in read append form 
# (r read r+ Read and append) and encoding 
#scheme as utf-8 and storing the object made as file
    with open(user_input, 'r+', encoding='utf-8') as file:
        # Creating a dictionary to store key and values
        dictionary_for_words = {}
#Creating an empty set
        word_of_set = set(())
        lst = []
        #Looping meticulously line-by-line present in the file object
        for sentence in file:
#Replacing the new line with empty 
#space as we do not need new line to be in user readable lists/sets
            sentence = sentence.replace('\n', '') 
 #Adding the sentence to the set words_of_set
            word_of_set.add(sentence)
#Add the sentence to a list also
            lst.append(sentence)
#As set stores unique values only words_of_set contains unique values
        print('All the unique words', len(word_of_set))
 #Looping through sentences present in list 1st
        for word in lst:
 # Now checking if the word contains characters greater than 4.
            if len(word) > 4:
 # Checking if the word is present in the dictionary or not.
                if word not in dictionary_for_words.keys():
 # if it is not present, create a new element in the dicionary
                    dictionary_for_words[word] = 1
                else:
# Add to the value incrementally for the word if it already
#present in the dicionary
                    dictionary_for_words[word] += 1
# dictionary_for_words.item() will return the list of set of key value pairs f.ex 
#(...[(key1,value1), (key2,value2)]. Using lambda funtion sorting items based on the value (x[0] is 
# is key x[1] is corresponding value) reverse=True implies to sort in decreasing order (by default storing
# in increasing order).
        All_value = sorted(dictionary_for_words.items(), key=lambda x: x[1], reverse=True)
        print('\n Top 10 most used words')
# Now print the first 10 elements earlier sorted in decreasing order.
        for i in range(10):
            print(All_value[i])

print('Life of Brian')
count_the_all_un_words(Brain_file, supreme_route)
print('Swedish News')
count_the_all_un_words(Swedish_file, supreme_route)
