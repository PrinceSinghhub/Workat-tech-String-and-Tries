class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')

        ans = ''
        for i in arr[::-1]:
            ans += i
            ans += ' '

        ans.strip()
        return ans






