class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = list(s);
        left = 0;
        right = len(s)-1;
        vowels = ['a','e','i','o','u','A','E','I','O','U'];
        while left < right :
            while left < right and lst[left] not in vowels:
                left += 1;
            while left < right and lst[right] not in vowels:
                right -= 1;
            lst[left], lst[right] = lst[right], lst[left];
            left += 1;
            right -= 1;
    
        return("".join(lst))