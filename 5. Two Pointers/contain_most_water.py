def maxArea(height):
    n = len(height)
    start = 0
    end = n-1
    area = 0
    while start < end:
        area = max(area, min(height[start], height[end])*(end-start))
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
    return area


print(maxArea(height=[6, 11, 7, 4, 7, 1, 3, 8, 10, 10, 7, 2]))
