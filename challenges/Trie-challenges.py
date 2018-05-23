import time
import re
import random
import pdb


def get_words(file):
    with open(file, 'r') as f:
        word_list = f.read().lower().split()
        word_list.sort()
    return word_list


def autocomplete(prefix, lst):
    """return all words that start with prefix
    Ex: autocomplete('appl') => ['apple', 'application', ...]"""
    prefix_length = len(prefix)
    complete_words = []
    index = binary_search_recursive(lst, prefix)
    left_word = ""
    right_word = ""
    left = index - 1
    right = index + 1
    left_word = lst[left]
    # if right < len(lst) - 1:
    right_word = lst[right]
    if prefix == "":
        return complete_words
    if lst[index].startswith(prefix):
        complete_words.append(lst[index])
    while left_word.startswith(prefix) or right_word.startswith(prefix):
        if left_word.startswith(prefix):
            complete_words.append(left_word)
            left -= 1
            left_word = lst[left]

        if right_word.startswith(prefix):
            complete_words.append(right_word)
            right += 1
            if right < len(lst) - 1:
                right_word = lst[right]

        if left > right:
            return complete_words
    print(complete_words)
    return complete_words


def binary_search_recursive(array, item, left=None, right=None):
    # implement binary search recursively here

    # Setting the left and right index
    # Left index is the 0
    # Right index is the
    if left is None and right is None:
        left = 0
        right = (len(array) - 1)

    # Middle is the left + right index / 2
    middle = int((left + right) / 2)
    middle_item = array[middle]
    item_len = len(item)
    left_item = array[left]
    right_item = array[right]

    # If item is equal the middle index of the array return index
    if middle_item[:item_len] == item:
        return middle

    # If middle item is less than item the move the left index plus one
    if middle_item[:item_len] < item:
        left = middle + 1

    # If middle item is more than item the move the left index plus one
    if middle_item[:item_len] > item:
        right = middle - 1

    # If the left index surpassed the right index then return None
    if left > right:
        return right

    return binary_search_recursive(array, item, left, right)


def benchmark(all_prefixes, all_words):
    t1 = time.time()
    for i in all_prefixes:
        # pdb.set_trace()
        # print("This is the prefix: {}".format(i))
        autocomplete(i, all_words)
    t2 = time.time()
    benchmark_time = t2 - t1
    return benchmark_time


if __name__ == '__main__':
    all_words = get_words('/usr/share/dict/words')
    all_prefixes = set([word[:len(word)//2] for word in all_words])
    # print(all_prefixes)
    # some_prefixes = []
    # for i in range(0, 10):
    #     some_prefixes.append(all_words[i])
    time = benchmark(all_prefixes, all_words)
    # words = autocomplete('a')
    # print('There are the word prefixes {}'.format(words))
    print('Took {} seconds to benchmark {} prefixes on {} words'.format(time, len(all_prefixes), len(all_words)))
