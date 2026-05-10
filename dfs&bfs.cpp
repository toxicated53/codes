#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<int> graph[10];
bool visited[10];

// DFS Function
void dfs(int node)
{
    visited[node] = true;

    cout << node << " ";

    for(int neighbour : graph[node])
    {
        if(!visited[neighbour])
        {
            dfs(neighbour);
        }
    }
}

// BFS Function
void bfs(int start)
{
    queue<int> q;

    q.push(start);

    visited[start] = true;

    while(!q.empty())
    {
        int node = q.front();

        q.pop();

        cout << node << " ";

        for(int neighbour : graph[node])
        {
            if(!visited[neighbour])
            {
                visited[neighbour] = true;

                q.push(neighbour);
            }
        }
    }
}

int main()
{
    int vertices, edges;

    cout << "Enter number of vertices: ";
    cin >> vertices;

    cout << "Enter number of edges: ";
    cin >> edges;

    cout << "Enter edges:\n";

    for(int i = 0; i < edges; i++)
    {
        int u, v;

        cin >> u >> v;

        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int start;

    cout << "Enter starting vertex: ";
    cin >> start;

    // DFS
    cout << "\nDFS Traversal: ";

    dfs(start);

    // Reset visited array
    for(int i = 0; i < 10; i++)
    {
        visited[i] = false;
    }

    // BFS
    cout << "\nBFS Traversal: ";

    bfs(start);

    return 0;
}
