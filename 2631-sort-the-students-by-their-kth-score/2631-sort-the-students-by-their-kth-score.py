class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        students = list(range(len(score)))

        results = {}
        for i in students:
            _ = score[i][k]
            results[_] = score[i]
        
        results = dict(sorted(results.items(), reverse=True))
        L = []
        for key,value in results.items():
            L.append(value)
        return L