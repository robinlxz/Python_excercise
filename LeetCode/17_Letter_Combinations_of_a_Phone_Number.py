#url:https://leetcode.com/problems/letter-combinations-of-a-phone-number/

#By myself (1st time), 2019 Feb 10th. (faster than 8% only)

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res = []
        def dfs(s,p):
            if s == '':
                if p == '': return
                res.append(p)
            else:
                for i in letters[int(s[0])]:
                    dfs(s[1:],p+i)

        dfs(digits,'')
        return res

def main():
    A = Solution()
    print A.letterCombinations('')

if __name__ == '__main__':
    main()