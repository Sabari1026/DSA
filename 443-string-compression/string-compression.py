class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0   
        j = 0   
        while j < len(chars):
            char = chars[j]
            count = 0
            while j < len(chars) and chars[j] == char:
                j += 1
                count += 1
            chars[i] = char
            i += 1
            if count > 1:
                for c in str(count):
                    chars[i] = c
                    i += 1
        return i
        