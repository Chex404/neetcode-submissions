class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_list = []
        output = []
        used = [False] * len(strs)

        for word in strs:
            sorted_list.append(''.join(sorted(word)))

        for i in range(len(strs)):
            if used[i]:
                continue

            l = [strs[i]]
            used[i] = True

            for j in range(i + 1, len(strs)):
                if sorted_list[i] == sorted_list[j]:
                    l.append(strs[j])
                    used[j] = True

            output.append(l)

        return output