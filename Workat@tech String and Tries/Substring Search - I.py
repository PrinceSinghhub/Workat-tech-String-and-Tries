class Solution:
    def findStartIndexOfSubstring(self, s1: str, s2: str) -> int:

        if len(s2) > len(s1):
            return -1

        for i in range(len(s1) - len(s2)+1):
            temp = s1[i:len(s2)+i]
            if temp == s2:
                return i

        return -1

ans = Solution()

a = 'helloworld'
b = 'low'
print(ans.findStartIndexOfSubstring(a,b))


