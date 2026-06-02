class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            #     1       <=     1            10    <=   8
            if matrix[i][0] <= target and target <= matrix[i][n-1]:
                # print(matrix[i][0], matrix[i][n-1])
                r = n-1
                l = 0
                if r == l:
                    if matrix[i][l] == target:
                        return True
                    else:
                        return False

                while(r > l):
                    m = (r+l)//2
                    if matrix[i][m] == target or matrix[i][l] == target or matrix[i][r] == target:
                        return True
                    elif matrix[i][m] < target:
                        l = m + 1
                    else:
                        r = m
        return False