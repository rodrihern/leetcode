def trap(height: list[int]) -> int:
    # we compute highest at the left and highest at the right 
    # then once we have that we can do min(l, r) - h and we add that to the sum
    res = 0

    highest = 0
    left_max = []
    for h in height:
        left_max.append(highest)
        highest = max(highest, h)
    
    highest = 0
    right_max = [0] * len(height)
    for i in range(len(height)-1, -1, -1):
        right_max[i] = highest
        highest = max(highest, height[i])

    for i in range(len(height)):
        current = min(left_max[i], right_max[i]) - height[i]
        if current > 0:
            res += current

    return res