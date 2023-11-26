def maxArea(height):
    n = len(height)
    start = 0
    end = n-1
    area = 0
    while start < end:
        area = max(area, min(height[start], height[end])*(end-start))
        if height[start] < height[end]:
            start += 1
        elif height[start] > height[end]:
            end -= 1
        else:
            start += 1
            end -= 1
    return area


print(maxArea(height=[6, 11, 7, 4, 7, 1, 3, 8, 10, 10, 7, 2]))
