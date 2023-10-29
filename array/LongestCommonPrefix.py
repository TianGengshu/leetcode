class Solution:
    def longestCommonPrefix(self, strs ) -> str:
        if not strs:
            return ""

        # Using the first word to compare with the rest
        for i in range(len(strs[0])):
            # iterate over the rest
            for string in strs[1:]:

                # If not the same in the same index, return directly
                # Careful for index out of range
                if i >= len(string) or strs[0][i] != string[i]:
                    return strs[0][:i]

        return strs[0]


if __name__ == '__main__':
    s = Solution()

    print(s.longestCommonPrefix(["ab","abc"]))