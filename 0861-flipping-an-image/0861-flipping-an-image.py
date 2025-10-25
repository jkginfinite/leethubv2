class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flipped = []
        n = len(image)
        for row in range(n):
            flipped.append(image[row][::-1])
        
        inverted = []
        for row in range(n):
            r = []
            for col in range(n):
                _ = flipped[row][col]
                if _==1:
                    r.append(0)
                else:
                    r.append(1)
            inverted.append(r)
        return inverted

        