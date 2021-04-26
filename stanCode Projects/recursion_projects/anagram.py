"""
File: anagram.py
Name: Ruby
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
word_lst = []


def main():
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    while True:
        word = input("Find anagrams for: ")
        if word == EXIT:
            break
        read_dictionary()
        find_anagrams(word)


def read_dictionary():
    global word_lst
    with open(FILE, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                word_lst.append(word)


def find_anagrams(s):
    """
    :param s: str, input word
    """
    count_lst = []
    chosen_words = []
    chosen_lst = []
    pop_out_words(s, chosen_lst)
    helper(s, chosen_words, count_lst, '', [], chosen_lst)
    print(str(sum(count_lst)), 'anagrams: ', chosen_words)


def pop_out_words(input_word, chosen_lst):
    """
    :param input_word: str, input word
    :param chosen_lst: list, a list to put only words that has same length or composite letters as the input word
    """
    global word_lst
    for words in word_lst:
        num = 0
        if len(words) != len(input_word):
            pass
        else:
            for digit in words:
                if digit not in input_word:
                    break
                else:
                    num = num + 1
            if num >= len(input_word):
                chosen_lst.append(words)


def helper(word, chosen_words, count_lst, str, num_lst, chosen_lst):
    """
    :param word: str, input word
    :param chosen_words: list, save words that is anagram to the input word
    :param count_lst: list, count numbers of anagrams
    :param str: str, temporary string to save characters in input word
    :param num_lst: list, to save number i
    """
    if len(str) == len(word):
        print('Searching...')
        print('Found: ' + str)
        if str not in chosen_words:
            chosen_words.append(str)
            count_lst.append(1)
    else:
        for i in range(len(word)):
            if i in num_lst:
                pass
            else:
                # Choose
                str = str + word[i]
                num_lst.append(i)
                # Explore
                if has_prefix(str, chosen_lst) == True:
                    helper(word, chosen_words, count_lst, str, num_lst, chosen_lst)
                # Un-choose
                str = str[:-1]
                num_lst.pop()


def has_prefix(sub_s, chosen_lst):
    """
    :param sub_s: str, check if word starts with sub_s
    :return: bool, True or False
    """
    for word in chosen_lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
