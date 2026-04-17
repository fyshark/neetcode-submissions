class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for s in strs:
            sSorted = "".join(sorted(s))
            my_dict[sSorted].append(s)
        return list(my_dict.values())