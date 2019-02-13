#!/usr/bin/env python
'''
url: https://leetcode.com/problems/letter-case-permutation/

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]

Note:
S will be a string with length between 1 and 12.
S will consist only of letters or digits.
'''

import string


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        l_all=[]
        list_to_return = []
        for i in range(len(S)):
            if S[i] in string.ascii_letters:
                #print 'S[i] is', S[i]
                #print 'i is', i
                #print 'S[i].lower is', S[i].lower
                #print '[S[i].lower, S[i].upper] is', [S[i].lower, S[i].upper]
                l_all.append([S[i].lower(), S[i].upper()])
                #print l_all[0]
            else:
                l_all.append([S[i]])
        #print len(l_all)
        #print l_all[3]
        if len(S) == 4:
            for a0 in l_all[0]:
                for a1 in l_all[1]:
                    for a2 in l_all[2]:
                        for a3 in l_all[3]:
                            print a0+a1+a2+a3
                            list_to_return.append(a0+a1+a2+a3)

        return list_to_return


'''Below is one of answer online'''

class Solution2(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []

        def helper(s, p):
            if s == "":
                res.append(p)
                return
            if s[0].isdigit():
                helper(s[1:], p + s[0])
            else:
                helper(s[1:], p + s[0].upper())
                helper(s[1:], p + s[0].lower())

        helper(S, "")
        return res









'''rewrite by l'''
class Solution3(object):
    def letterCasePermutation(self, S):
        res = []
        def helper(s, p):
            if s == "":
                res.append(p)
                return
            elif s[0].isdigit():
                helper(s[1:], p+s[0])
            else:
                helper(s[1:], p + s[0].lower())
                helper(s[1:], p + s[0].upper())

        helper(S,"")
        return res

A = Solution3()
print A.letterCasePermutation('a78S7')