#url: https://leetcode.com/problems/generate-parentheses/

#My code is out of time limit
class Solution(object):
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


# n=1
# res_d = {}
# s = ''
# for i in range(len(s)+1):
#     s_1 = s[:i]+ '(' + s[i:]
#     for j in range (i+1,len(s_1)+1):
#         s_2 = s_1[:j]+ ')' + s_1[j:]
#         res_d[s_2] = 1

# Solution online
# https://leetcode.com/problems/generate-parentheses/discuss/10096/4-7-lines-Python

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
    #A = Solution2()
    #print A.generateParenthesis(3)
    test()

def test():
    '''
    This is about 'generators' for yield
    url: https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
    :return:
    '''
    for i in range(3):
        yield i
a = test()
for i in a:
    print i

if __name__ == '__main__':
    main()