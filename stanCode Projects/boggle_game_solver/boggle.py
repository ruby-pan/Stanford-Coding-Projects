"""
File: boggle.py
Name: Ruby
----------------------------------------
A famous game named Boggle that looks for all possible combination of words in a 4x4 square of letters.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
word_lst = []


def main():
    """
    Gets 4x4 input letters and goes to find_boggle function to find words that match.
    """
    chart_list = []
    num = 0
    for i in range(4):
        line = input(str(i + 1) + ' row of letters: ')
        line = line.split()
        for j in line:
            if len(j) >= 2:
                num += 1
        if len(line) != 4 or num >= 1:  # 打了超過四組字母or一格打太多字母
            print('Illegal format.')
            break
        chart_list.append(line)
    read_dictionary()
    find_boggle(chart_list)


def find_boggle(chart_lst):
    count_lst = []
    chosen_words = []
    chosen_lst = []
    num = 0
    pop_out_words(chart_lst, chosen_lst)
    for x in range(4):
        for y in range(4):
            pre_val = [(x,y)]
            helper('', pre_val, chart_lst, count_lst, x, y, num, chosen_words, chosen_lst)
    print('There are', str(sum(count_lst)), 'in total.')


def pop_out_words(chart_lst, chosen_lst):
    """
    This function collects all letters from chart_lst and check if words in the dictionary has letters
    that doesn't appear in the chart_lst.
    """
    global word_lst
    string = ''
    for row in chart_lst:
        for letter in row:
            string = string + letter
    for word in word_lst:
        num = 0
        for digit in word:
            if digit not in string:
                break
            else:
                num += 1
            if num == len(word):
                if word not in chosen_lst:
                    chosen_lst.append(word)


def helper(temporary_str, pre_val, chart_lst, count_lst, x, y, num, chosen_words, chosen_lst):
    """
    :param temporary_str: (str) Temporary string to save current combination of letters
    :param pre_val: (list) A list of tuples to save the previous route (x, y)
    :param chart_lst: (list) The input 4x4 letters
    :param count_lst: (list) To count how many words found
    :param x & y: (int) 4x4
    :param chosen_words: (list) A list to save matched words
    :param chosen_lst: (list) A minimized word_lst
    """
    if temporary_str in chosen_lst and temporary_str not in chosen_words:
        print('Found "' + temporary_str + '"')
        chosen_words.append(temporary_str)
        count_lst.append(1)

    if num == 0:    # 第一顆進來的
        temporary_str = temporary_str + chart_lst[x][y]
        num += 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x + i < 0 or y + j < 0 or x + i >= 4 or y + j >= 4:  # 超過邊框
                pass
            elif i == 0 and j == 0:    # 不能加入自己
                pass
            elif (x+i, y+j) in pre_val:   # 不能回頭走
                pass
            else:
                search_letter = chart_lst[x + i][y + j]
                search_letter.lower()
                # Choose
                temporary_str = temporary_str + search_letter
                # Explore
                if has_prefix(temporary_str, chosen_lst) == True:
                    pre_val.append((x,y))
                    x = x + i
                    y = y + j
                    helper(temporary_str, pre_val, chart_lst, count_lst, x, y, num, chosen_words, chosen_lst)
                    x = x - i
                    y = y - j
                    pre_val.pop()
                # Un-choose
                temporary_str = temporary_str[:-1]


def has_prefix(sub_s, chosen_lst):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in chosen_lst:
        if word.startswith(sub_s):
            return True
    return False


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    global word_lst
    with open(FILE, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(word) >= 4:
                    word_lst.append(word)


if __name__ == '__main__':
    main()
