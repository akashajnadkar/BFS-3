'''
Time Complexity - Exponential
Space Complexity - O(n^n)

Works on leetcode
'''
from collections import deque
class Solution:
    def __init__(self):
        self.result = []
        self.childSet = set()
        self.maxSize = 0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        # DFS
        # self.dfs(s)
        # return self.result
        queue = deque()
        queue.append(s)
        #maintain a flag to stop proceeding to next level when valid string found
        flag = False
        while queue and not flag:
            size = len(queue) #maintain a size for each level
            for i in range(size):
                string = queue.popleft() #pop the next string from queue
                #check if its valid, if yes add to result and set flag to True
                if self.isValid(string):
                    flag = True
                    self.result.append(string)
                #if not valid generate children by removing character one by one from every index and add to queue
                if not flag:
                    for i in range(len(string)):
                        if string[i].isalpha():
                            continue
                        child = string[0:i] + string[i+1:]
                        if child not in self.childSet:
                            #before add child to queue check if it has been added before
                            self.childSet.add(child)
                            queue.append(child)
        return self.result
    
    
    def dfs(self, s):
        #basecases
        if len(s) < self.maxSize:
        #once length goes below max Size we prevent from going deeper
            return
        if self.isValid(s):
            #maintain a max Size to prevent going deeper and check validity and also length
            if self.maxSize<len(s):
                self.maxSize = len(s)
                self.result = []
            self.result.append(s)
            return

        #logic
        for i in range(len(s)):
            if s[i].isalpha():
                continue
            child = s[0:i] + s[i+1:]
            if child not in self.childSet:
                #check if child has been traversed before recursing
                self.childSet.add(child)
                self.dfs(child)

    def isValid(self, s)->bool:
        counter = 0
        for c in s:
            if c == "(":
                counter+=1
            elif c.isalpha():
                continue
            else:
                if counter == 0:
                    return False
                else:
                    counter-=1
        return True if counter == 0 else False


        