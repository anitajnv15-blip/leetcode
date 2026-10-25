class Solution(object):
    def kWeakestRows(self, mat, k):
        rows = []
        for i in range(len(mat)):
            soldiers = sum(mat[i])
            rows.append((soldiers,i))
        rows.sort()
        answer = []
        for i in range(k):
            answer.append(rows[i][1])
        return answer

        