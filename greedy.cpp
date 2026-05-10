#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cout<<"enter total number of elements";
    cin>>n;
    cout<<endl;
    cout<<"enter elements";
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    // selection dort
    for(int i=0;i<n;i++)
    {
        int minindex = i;
        for(int j=i+1;j<n;j++)
        {
            if(arr[j]<arr[minindex])
            {
                minindex=j;
            }
        }
        swap(arr[i],arr[minindex]);
    }
    cout<<"SORTED ARRAY"<<endl;

    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }

    return 0;
}

//job scheduling algorithms
#include <iostream>
#include <algorithm>

using namespace std;

struct Job
{
    char id;
    int deadline;
    int profit;
};

bool compare(Job a, Job b)
{
    return a.profit > b.profit;
}

int main()
{
    int n;

    cin >> n;

    Job jobs[n];

    for(int i = 0; i < n; i++)
    {
        cin >> jobs[i].id
            >> jobs[i].deadline
            >> jobs[i].profit;
    }

    sort(jobs, jobs + n, compare);    // or we can write it as sort(&jobs[0],&jobs[n],compare);

    bool slot[10] = {false};

    for(int i = 0; i < n; i++)
    {
        for(int j = jobs[i].deadline - 1; j >= 0; j--)
        {
            if(!slot[j])
            {
                slot[j] = true;

                cout << jobs[i].id << " ";

                break;
            }
        }
    }

    return 0;
}
