class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True


s = Solution()
assert s.isPalindrome("amanaplanacanalpanama") is True
assert s.isPalindrome("abba") is True
assert s.isPalindrome("aba") is True
assert s.isPalindrome("soidjfi") is False
assert s.isPalindrome("A man, a plan, a canal: Panama") is True

print('pass')
