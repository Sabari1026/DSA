class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        lst = []
        for i in range(len(candies)):
            new = candies[i] + extraCandies
            if new >= max(candies):
                lst.append(True)
            else:
                lst.append(False)
        return lst