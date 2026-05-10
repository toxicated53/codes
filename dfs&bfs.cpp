#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// DFS Function
void dfs(int node, vector<vector<int>>& adj, vector<bool>& visited)
{
    visited[node] = true;

    cout << node << " ";

    for(int neighbor : adj[node])
    {
        if(!visited[neighbor])
        {
            dfs(neighbor, adj, visited);
        }
    }
}

// BFS Function
void bfs(int start, vector<vector<int>>& adj, vector<bool>& visited)
{
    queue<int> q;

    q.push(start);

    visited[start] = true;

    while(!q.empty())
    {
        int node = q.front();

        q.pop();

        cout << node << " ";

        for(int neighbor : adj[node])
        {
            if(!visited[neighbor])
            {
                visited[neighbor] = true;

                q.push(neighbor);
            }
        }
    }
}

int main()
{
    int n, m;

    cout << "Enter number of vertices: ";
    cin >> n;

    cout << "Enter number of edges: ";
    cin >> m;

    vector<vector<int>> adj(n);

    cout << "Enter edges (u v):" << endl;

    for(int i = 0; i < m; i++)
    {
        int u, v;

        cin >> u >> v;

        adj[u].push_back(v);
        adj[v].push_back(u); // Undirected graph
    }

    int start;

    cout << "Enter starting vertex: ";
    cin >> start;

    // DFS
    vector<bool> visited1(n, false);

    cout << "\nDFS Traversal: ";

    dfs(start, adj, visited1);

    // BFS
    vector<bool> visited2(n, false);

    cout << "\nBFS Traversal: ";

    bfs(start, adj, visited2);

    return 0;
}
