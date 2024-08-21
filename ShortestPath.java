/*You are given an Undirected Graph having unit weight of the edges, find the shortest path from src to all the vertex and
if it is unreachable to reach any vertex, then return -1 for that vertex.*/

class Solution {
    
    public int[] shortestPath(int[][] edges, int n, int m, int src) {
        // Step 1: Build the adjacency list representation of the graph
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        
        // Step 2: Initialize distances and queue for BFS
        int[] dist = new int[n];
        Arrays.fill(dist, -1);  // Initialize distances as -1 (unreachable)
        Queue<Integer> queue = new LinkedList<>();
        
        // Step 3: Start BFS from the source vertex
        dist[src] = 0;
        queue.add(src);
        
        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int v : adj.get(u)) {
                if (dist[v] == -1) {  // Not visited
                    dist[v] = dist[u] + 1;
                    queue.add(v);
                }
            }
        }
        
        return dist;
    }
}
