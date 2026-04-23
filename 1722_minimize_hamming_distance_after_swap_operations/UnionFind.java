public class UnionFind {
    int[] parent;
    int[] rank;

    public UnionFind(int n) {
        this.parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        this.rank = new int[n]; 
    }

    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    public void union(int x, int y) {
        x = find(x);
        y = find(y);

        if (x == y) {
            return;
        }

        if (rank[x] < rank[y]) {
            int tmp = x;
            x = y;
            y = tmp;
        }

        parent[y] = x;
        if (rank[x] == rank[y]) {
            rank[x] += 1;
        }
    }


}
