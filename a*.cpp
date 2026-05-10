#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct State
{
    vector<vector<int>> board;
    int x, y;   // blank position
    int cost;
};

// Print puzzle
void printBoard(vector<vector<int>> board)
{
    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            cout << board[i][j] << " ";
        }

        cout << endl;
    }

    cout << endl;
}

int main()
{
    State start;

    cout << "Enter 8 puzzle (use 0 for blank):\n";

    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            cin >> start.board[i][j];

            if(start.board[i][j] == 0)
            {
                start.x = i;
                start.y = j;
            }
        }
    }

    queue<State> q;

    q.push(start);

    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};

    cout << "\nPossible Moves:\n";

    while(!q.empty())
    {
        State current = q.front();

        q.pop();

        printBoard(current.board);

        for(int i = 0; i < 4; i++)
        {
            int nx = current.x + dx[i];
            int ny = current.y + dy[i];

            if(nx >= 0 && ny >= 0 && nx < 3 && ny < 3)
            {
                State next = current;

                swap(next.board[current.x][current.y],
                     next.board[nx][ny]);

                next.x = nx;
                next.y = ny;

                q.push(next);
            }
        }

        break; // only first expansion
    }

    return 0;
}
