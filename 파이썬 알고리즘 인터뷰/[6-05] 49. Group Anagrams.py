"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""
from typing import List
import collections
from itertools import groupby


def groupAnagrams(strs: List[str]) -> List[List[str]]:

    # 1. 정렬된 단어 tuple로 묶기
    word_tuple = sorted([(word, "".join(sorted(list(word)))) for word in strs], key=lambda x: x[1], reverse=False)
    word_tuple = [(j, i) for (i, j) in word_tuple]

    groups = []

    for key, group in groupby(word_tuple, lambda x: x[0]):
        g = []
        for k, elem in group:
            print(k, elem)
            g.append(elem)
        groups.append(g)

    return groups


def simple_groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(list(word)))].append(word)
        print(anagrams)

    return anagrams.values()


if __name__=='__main__':
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(simple_groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))