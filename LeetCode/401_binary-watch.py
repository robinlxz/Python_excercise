#!/usr/bin/env python

'''
https://leetcode.com/problems/binary-watch/
'''


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        oct(0b0110)
        bin(16)
        if num == 0:
            return ['0:00']

        #if num == 1:
        #binary_minute = 0001, 0010, how?
        minute = oct(binary_minute)





#one solution (https://leetcode.com/problems/binary-watch/discuss/88453/Python-DFS-and-complexity-analysis)
class Solution_A(object):
    def readBinaryWatch(self, n):

        def dfs(n, hours, mins, idx):
            if hours >= 12 or mins > 59: return
            if not n:
                res.append(str(hours) + ":" + "0" * (mins < 10) + str(mins))
                return
            for i in range(idx, 10):
                if i < 4:
                    dfs(n - 1, hours | (1 << i), mins, i + 1)
                else:
                    k = i - 4
                    dfs(n - 1, hours, mins | (1 << k), i + 1)

        res = []
        dfs(n, 0, 0, 0)
        return res



class Test():
    def readBinary(self,n):
        res = []
        def dfs(n,hours,idx):
            if hours > 12:
                return
            if not n:
                res.append(bin(hours))
            else:
                for i in range(idx,4):
                    dfs(n-1, hours|1<<i, i+1)
        dfs(n,0,0)
        return res


class Solution_l():
    def readBinaryWatch(self,n):
        res = []
        def dfs(n, hours, mins, idx):
            if hours >= 12 or mins >= 60:
                return
            if not n:
                if mins < 10:
                    mins = '0'+str(mins)
                res.append(str(hours)+':'+str(mins))
            else:
                for i in range(idx,10):
                    if i < 4:
                        dfs(n-1,hours|1<<i,mins,i+1)
                    else:
                        j = i -4
                        dfs(n-1,hours,mins|1<<j,i+1)
        dfs(n,0,0,0)
        return res

class Solution_l2():
    def readBinaryWatch(self,n):
        res = []
        def dfs(n, hours, mins, idx):
            if hours >= 12 or mins >= 60:
                return
            if not n:
                if mins < 10:
                    mins = '0'+str(mins)
                res.append(str(hours)+':'+str(mins))
            else:
                for i in range(idx,10):
                    if i < 6:
                        dfs(n-1,hours,mins|1<<i,i+1)
                    else:
                        j = i -6
                        dfs(n-1,hours|1<<j,mins,i+1)
        dfs(n,0,0,0)
        return res

def main():
    #A = Solution_A()
    #print A.readBinaryWatch(2)
    #B = Test()
    #print B.readBinary(2)
    C = Solution_l2()
    print C.readBinaryWatch(1)
    print C.readBinaryWatch(8)

if __name__ == '__main__':
    main()