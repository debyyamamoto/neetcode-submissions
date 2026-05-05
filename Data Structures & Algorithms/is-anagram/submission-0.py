class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in dict_s:
                k = dict_s[i]
            else:
                k = 0
            dict_s[i] = k +  1
        for j in t:
            if j in dict_t:
                k = dict_t[j]
            else:
                k = 0
            dict_t[j] = k + 1
        for i in s:
            if dict_s.get(i, 0) == dict_t.get(i,0):
                continue
            else:
                return False
        return True