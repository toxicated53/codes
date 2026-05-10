#include <iostream>
using namespace std;

int board[10], n;

// Check if queen can be placed
bool safe(int row, int col)
{
    for(int i = 0; i < row; i++)
    {
        // Same column OR diagonal
        if(board[i] == col || abs(board[i] - col) == abs(i - row))
        {
            return false;
        }
    }

    return true;
}

// Backtracking function
void solve(int row)
{
    if(row == n)
    {
        cout << "\nSolution:\n";

        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(board[i] == j)
                    cout << "Q ";
                else
                    cout << ". ";
            }

            cout << endl;
        }

        return;
    }

    for(int col = 0; col < n; col++)
    {
        if(safe(row, col))
        {
            board[row] = col;

            solve(row + 1);
        }
    }
}

int main()
{
    cout << "Enter number of queens: ";
    cin >> n;

    solve(0);

    return 0;
}
