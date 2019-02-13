#url: https://leetcode.com/problems/generate-parentheses/

#My code is out of time limit
class Solution1_overtime(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res_d = {}
        def dfs(n,s):
            if not n:
                res_d[s] = 1
            else:
                for i in range(len(s) + 1):
                    s_1 = s[:i] + '(' + s[i:]
                    for j in range(i + 1, len(s_1) + 1):
                        s_2 = s_1[:j] + ')' + s_1[j:]
                        dfs(n-1,s_2)
        dfs(n,'')
        return res_d.keys()

#Solution rewrite
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        def dfs(left,right,string):
            if right<left:
                return
            if not left and not right:
                res.append(string)
                return
            if left:
                dfs(left-1,right,string+'(')
            if right:
                dfs(left,right-1,string+')')
        dfs(n,n,'')
        return res




# Solution online
# https://leetcode.com/problems/generate-parentheses/discuss/10096/4-7-lines-Python
# !!! Best way to understand is draw a figure shows how dfs call itself with each branch (if), and how it return. 20190212
class Solution2(object):
    def generateParenthesis(self, n):
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left - 1, right):
                    yield q
                for q in generate(p + ')', left, right - 1):
                    yield q

        return list(generate('', n, n))

def main():
    A = Solution()
    print A.generateParenthesis(2)

if __name__ == '__main__':
    main()