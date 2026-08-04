class Solution(object):
    def finalValueAfterOperations(self, operations):
        a = "--X"
        b = "X++"
        c = "X--"
        d = "++X"
        x = 0
        for i in range(len(operations)):
            if operations[i] == a or operations[i] == c:
                x = x - 1
            elif operations[i] == b or operations[i] == d :
                x = x + 1
            
        return x
