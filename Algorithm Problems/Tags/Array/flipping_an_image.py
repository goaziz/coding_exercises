from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        image = [i[::-1] for i in image]

        for i in range(len(image)):
            for j in range(len(image)):
                if image[i][j] == 0:
                    image[i][j] = 1
                elif image[i][j] == 1:
                    image[i][j] = 0
        return image


# other solution
class Solution2:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for row in image:
            result.append(list(map(lambda x: 0 if x == 1 else 1, row[::-1])))
        return result
