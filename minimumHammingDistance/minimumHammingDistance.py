
from typing import List
from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)

        for swap in allowedSwaps:
            uf.union(swap[0], swap[1])

        freq = defaultdict(lambda: defaultdict(int))
        for i, value in enumerate(source):
            group = uf.find(i)
            freq[group][value] += 1

        # now what I need to do is to see how many matches in each group
        distance = n
        for i, value in enumerate(target):
            group = uf.find(i)
            if freq[group][value] > 0:
                distance -= 1
                freq[group][value] -= 1



        return distance