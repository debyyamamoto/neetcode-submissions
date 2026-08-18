class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        ind = 0
        tam = len(strs) - 1
        if tam == 0:
            return strs[0]
        
        for i in strs[0]: 
            c = 0
            for j in strs[1:]:
                if ind >= len(j):
                    return "".join(ans)
                c += 1
                print({i}, {j[ind]}, {ind}, {c}, {tam})
                if i == j[ind] and c == tam:
                    ind += 1
                    ans.append(i)
                elif i != j[ind]:
                    return "".join(ans)
        return "".join(ans)