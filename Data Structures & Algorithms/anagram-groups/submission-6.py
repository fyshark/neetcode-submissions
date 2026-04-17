class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))
            my_dict[sortedS].append(s)
        return list(my_dict.values())