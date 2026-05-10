#include <iostream>
using namespace std;

int main()
{
    string userinput;
    cout<<"Customer Support Chatbot "<<endl;
    cout<<"Type exit to end the chat"<<endl;

    while(true)
    {
            getline(cin,userinput);
            if(userinput == "hello" || userinput=="hi")
            {
                cout<<"Bot: Hello! How may i help you"<<endl;
            }
            else if(userinput == "product")
            {
                cout<<"Bot: We sell Laptps , mobiles and headphones"<<endl;
            }
            else if(userinput=="price")
            {
                cout<<"Bot: Prices start from 500 "<<endl;
            }
            else if(userinput == "delivery")
            {
                cout<<"Bot: Delivery takes upto 3 to 5 days "<<endl;
            }
            else if(userinput == "bye")
            {
                cout<<"Thank you for visiting "<<endl;
            }
            else if(userinput == "exit")
            {
                cout<<"Bot: Chat ended "<<endl;
                break;
            }
            else
            {
                cout<<"Sorry did not understand "<<endl;
            }
    }
    return 0;
}
