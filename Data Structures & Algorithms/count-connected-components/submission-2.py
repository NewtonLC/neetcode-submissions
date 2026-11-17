class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # In: Undirected graph, n nodes.
        # In: Edges array, edges[i] = [a,b]. a and b are nodes and edges[i] is the edge between them.
        # - Nodes are numbered 0 to n-1

        # Out: Int, total number of connected components in the graph.
        # - Connected component: Basically a subgroup of connected nodes.

        # This problem is a great example of the Union-Find algorithm! Let's use it to solve this problem.
        
        """
        Describing Union Find:

        We'll be maintaining two arrays: Parent and 

        Say we have 5 nodes: 0,1,2,3,4. Edges [[0,1],[1,2],[3,4]]
        Parent --> Starts off at [0,1,2,3,4]. Each index represents that node, each node starts off the 'parent' of itself.
        Rank --> [1,1,1,1,1]. Each index represents that node, each node starts off at rank '1', meaning they have no children.

        When we read [0,1], we note that 1 is a child of 0's parent. 1's parent becomes 0 and 0 becomes rank 2.
        Parent --> [0,0,2,3,4]
        Rank --> [2,1,1,1,1]

        [1,2], we note that 2 is a child of 1's parent. 2's parent becomes 0 and 0 becomes rank 3.
        Parent --> [0,0,0,3,4]
        Rank --> [3,1,1,1,1]

        [0,1], we note that 4 is a child of 3. 4's parent becomes 3 and 3 becomes rank 2.
        Parent --> [0,0,0,3,3]
        Rank --> [3,1,1,2,1]

        IF we encountered, say, [0,2], 2's parent and 0's parent are both 0, so they're already connected. No change is made.

        How can we write this into code?
        """

        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            # is res currently the same as par[n1]?
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1,n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        connected_components = n
        for n1, n2 in edges:
            connected_components -= union(n1, n2)
        
        return connected_components
