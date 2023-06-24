class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())
        if(len(s)%2==0):
            h1= s[:floor(len(s)/2.0)]
            h2=s[ceil(len(s)/2.0):]
        else:
            h1= s[:floor(len(s)/2.0)]
            h2=s[ceil(len(s)/2.0):]
        if h1 == h2[::-1]:
            return True
        else:
            return False
