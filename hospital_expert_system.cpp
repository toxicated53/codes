#include <iostream>
using namespace std;

int main()
{
    string fever, cough, headache;

    cout << "Do you have fever? (yes/no): ";
    cin >> fever;

    cout << "Do you have cough? (yes/no): ";
    cin >> cough;

    cout << "Do you have headache? (yes/no): ";
    cin >> headache;

    cout << "\nDiagnosis:\n";

    if(fever == "yes" && cough == "yes")
    {
        cout << "You may have Flu.";
    }

    else if(fever == "yes" && headache == "yes")
    {
        cout << "You may have Viral Fever.";
    }

    else if(cough == "yes")
    {
        cout << "You may have Cold.";
    }

    else
    {
        cout << "You seem healthy.";
    }

    return 0;
}
