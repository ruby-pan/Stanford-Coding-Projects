"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

The background coding of baby-name-search engine.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    if name in name_data:
        if year in name_data[name]:
            value = name_data[name][year]
            if int(rank) <= int(value):  # step3置換
                name_data[name][year] = rank
        else:
            name_data[name][year] = rank  # step2增加條件
    else:
        name_data[name] = {}
        name_data[name][year] = rank  # step1新人


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    with open(filename, 'r') as f:
        n = 0
        for line in f:
            data_line = line.split(',')
            if n == 0:      # 第一個是年分 year = ...
                year = data_line[0]
                year = year.strip()
                n += 1
            else:
                rank = data_line[0]
                name1 = data_line[1]
                name2 = data_line[2]

                rank = rank.strip()
                name1 = name1.strip()
                name2 = name2.strip()

                add_data_for_name(name_data, year, rank, name1)      #一次只有一筆(1990,1,H),(1990,2,B)...
                add_data_for_name(name_data, year, rank, name2)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for filename in filenames:
        add_file(name_data, filename)

    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    target = target.lower() #target是string
    names = []
    matching_names = []
    matching_names_capitalized = []

    for name in name_data:
        name = name.lower() #string
        names.append(name) #把一堆name都丟到list裡面

    # 現在有name data裡面的所有name的list,在進行兩個string的match
    for name in names:
        for i in range(len(name)-len(target)+1):
            sum = 0
            set = name[i:len(target)+i]
            for j in range(len(target)):
                if set[j] == target[j]:
                    sum += 1
                else:
                    sum += 0
            if sum >= len(target):
                matching_names.append(name)

    # matching_names 現在是一堆lower names的list -> 變大寫
    for name in matching_names:
        ans = ''
        for j in range(len(name)):
            char = name[j] # j=0 get 'a'
            if j == 0:
                char = char.upper()
                ans += char
            else:
                ans += char
        matching_names_capitalized.append(ans) # 放回

    return matching_names_capitalized


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
