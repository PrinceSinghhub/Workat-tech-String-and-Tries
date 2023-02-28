class Solution:
    def areAnagrams(self, A, B):

        if len(A) != len(B):
            return 0

        else:
            arrA = [0] * 26
            arrB = [0] * 26

            for i in range(len(A)):
                ai = ord(A[i]) - ord('a')
                bi = ord(B[i]) - ord('a')
                arrA[ai] += 1
                arrB[bi] += 1

            # if sum(arrA) == sum(arrB):
            #     return 1
            # return 0

            if arrA == arrB:
                return 1
            return 0
ans = Solution()
a = 'learn'
b = 'nerd'
print(ans.areAnagrams(a,b))


# pyhton code not support thats why use java code
'''
class Solution {
	boolean areAnagrams(String A, String B) {
		if(A.length() != B.length()) {
			return false;
		}
	    int hashA[] = new int[26];
		int hashB[] = new int[26];
		for(int i = 0; i < A.length(); i++) {
			hashA[A.charAt(i) - 'a']++;
			hashB[B.charAt(i) - 'a']++;
		}
		for(int i = 0; i < 26; i++) {
			if(hashA[i] != hashB[i]) {
				return false;
			}
		}
		return true;
	}
}
'''