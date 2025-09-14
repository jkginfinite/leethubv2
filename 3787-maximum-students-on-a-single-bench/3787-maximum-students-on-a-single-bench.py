class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        max_len = 0
        count = {}
        for s in students:
            student_id, bench_id = s
            if bench_id not in count:
                count[bench_id] = []
            if student_id not in count[bench_id]:
                count[bench_id].append(student_id)
            max_len = max(max_len,len(count[bench_id]))
        return max_len
        