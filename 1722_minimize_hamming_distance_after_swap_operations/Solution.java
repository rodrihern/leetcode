import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) {
        
        int n = source.length;
        UnionFind uf = new UnionFind(n);

        for (int[] swap : allowedSwaps) {
            uf.union(swap[0], swap[1]);
        }

        Map<Integer, Map<Integer, Integer>> groupFreqs = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int group = uf.find(i);
            groupFreqs.computeIfAbsent(group, k -> new HashMap<>()).merge(source[i], 1, Integer::sum);
            
        }

        int distance = n;

        for (int i = 0; i < n; i++) {
            int group = uf.find(i);
            if (groupFreqs.get(group).getOrDefault(target[i], 0) > 0 ) {
                distance--;
                groupFreqs.get(group).merge(target[i], 1, (x, y) -> x - y);
            }
        }
        
        return distance;
    }
}
