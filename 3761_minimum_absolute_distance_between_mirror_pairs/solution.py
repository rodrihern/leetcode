from typing import List


def minMirrorPairDistance(nums: List[int]) -> int:

    res = -1
    # lets reverse the numbers first so that we do not have to do it every time
    reversed_lookup = {}
    for i, n in enumerate(nums):
        if n in reversed_lookup:
            if res < 0:
                res = i - reversed_lookup[n]
            else:
                res = min(res, i - reversed_lookup[n])
        reversed_lookup[int(str(n)[::-1])] = i

    
    return res  

