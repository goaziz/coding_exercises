def binary_search(arr):
    min = 0
    max = len(arr) - 1
    b = -1

    while min <= max:
        mid = (max + min) // 2
        if arr[mid] < 0:
            b = mid
            max = mid - 1
        else:
            min = mid + 1
    return b


d = [4, 3, 2, -1]
print(binary_search(d))


class Solution:
    def countNegatives(self, grid):
        d = [x for b in grid for x in b if x < 0]

        return len(d)


# second option

def countNegatives(grid):
    count = 0
    for i in grid:
        bs = binary_search(i)
        print(bs)
        if bs >= 0:
            count += len(grid) - bs

    return count

# arr = [[1, -1], [-1, -1]]
# print(countNegatives(arr))
