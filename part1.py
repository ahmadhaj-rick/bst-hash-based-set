import os
#We initiate the program with the two text files in mind, that must be localized, identified, 
#read meticulously and then mainstreamed into the list.
#The Program is slated to identify the ten words based on the length , fruequency, uniquenessand 
#thereby loop them into the dictionary.A case in point, would be the unique words in the stated 
#guidelines for this program.

main_path = os.getcwd() # Getting the current path that will help integrate the 2 textfiles.
# Brain_file = 'life_of_13433_brian.txt'  # Fahim list
# Swedish_file = 'swe_16360080_news.txt'  # Fahim list

Brain_file = "brain_13335_words.txt"
Swedish_file = "swe_14133030_news"

def get_value(tpl): 
    return tpl[1]


def count_the_all_un_words(user_input, main_path):
    with open(user_input, 'r+', encoding='utf-8') as file:
        dictionary_for_words = {}
        word_of_set = set(())
        lst = []
        for sentence in file:
            sentence = sentence.replace('\n', '')
            word_of_set.add(sentence)
            lst.append(sentence)
        print('All the unique words', len(word_of_set))

        for word in lst:

            if len(word) > 4:
                if word not in dictionary_for_words.keys():
                    dictionary_for_words[word] = 1
                else:
                    dictionary_for_words[word] += 1

        All_value = sorted(dictionary_for_words.items(), key=lambda x: x[1], reverse=True)
        print('\n Top 10 most used words')

        for i in range(10):
            print(All_value[i])

print('Life of Brian')
count_the_all_un_words(Brain_file, main_path)
print('Swedish News')
count_the_all_un_words(Swedish_file, main_path)
