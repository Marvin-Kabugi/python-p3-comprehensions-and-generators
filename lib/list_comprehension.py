#!/usr/bin/env python3

def return_evens(num_list):
   return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list if sentence_list]

# print(return_evens(range(1,10, 2)))