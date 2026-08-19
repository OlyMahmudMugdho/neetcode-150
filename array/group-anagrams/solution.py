from typing import List 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for s in strs:
            key_arr = [0] * 26

            for letter in s:
                order = ord(letter.lower()) - 97
                key_arr[order] = key_arr[order] + 1

            key = str(key_arr)

            if hmap.get(key):
                hmap[key].append(s)
            else:
                hmap[key] = [s]



        return [val for val in hmap.values()]
