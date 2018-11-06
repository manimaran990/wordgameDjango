#!/usr/bin/python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from word_app.data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7

def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return random.sample(POUCH, NUM_LETTERS)


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    while True:
        word = input("Enter a word: ").upper()
        try:
            return _validation(word, draw)
        except ValueError as e:
            print(e)
            continue

def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    unused_words = list(draw)
    for ch in word:
        if ch in unused_words:
            unused_words.remove(ch)
        else:
            raise ValueError("{} one or more letters not in given letters".format(word))
    if word.lower() not in DICTIONARY:
        raise ValueError("{} not a dictionary word".format(word))
    return word


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char, 0) for char in word.upper())


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    permutations = [''.join(w).lower() for w in _get_permutations_draw(draw)]
    return set(permutations) & set(DICTIONARY)


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    for i in range(1, 8):
        yield from list(itertools.permutations(draw, i))


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


# def main():
#     """Main game interface calling the previously defined methods"""
#     while True:
#         user_input = int(input('''1. Play game\n2. Exit\n'''))                    
#         if user_input == 1:            
#             draw = draw_letters()
#             print('Letters drawn: {}'.format(', '.join(draw)))

#             word = input_word(draw)
#             word_score = calc_word_value(word)
#             print('Word chosen: {} (value: {})'.format(word, word_score))

#             possible_words = get_possible_dict_words(draw)

#             max_word = max_word_value(possible_words)
#             max_word_score = calc_word_value(max_word)
#             print('Optimal word possible: {} (value: {})'.format(
#                 max_word, max_word_score))

#             game_score = word_score / max_word_score * 100
#             print('You scored: {:.1f}'.format(game_score))
#         elif user_input == 2:
#             break        
#         else:
#             print("Invalid option..\n")
#             continue


# if __name__ == "__main__":
#     main()