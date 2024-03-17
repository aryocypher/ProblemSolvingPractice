class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        for i in range(len(strX)//2):
            if strX[i] != strX[len(strX)-1-i]:
                return False
        return True


class Solution2:
    def reverseNumber(self, x: int) -> int:
        rev = 0
        while x > 0:
            rev = rev*10 + x % 10
            x = x//10
        return rev

    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False

        rev = self.reverseNumber(x)
        print(rev)
        return rev == x
