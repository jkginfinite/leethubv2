class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        max_height = height
        for g in gain:
            height+=g
            max_height = max(max_height,height)
        return max_height