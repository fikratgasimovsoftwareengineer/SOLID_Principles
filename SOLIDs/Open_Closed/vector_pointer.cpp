#include <iostream>
#include <vector>
using namespace std;



class testPointer{

    private:

        vector <string> *ptr_Str;
    public:

        testPointer(){
            // initialize emty string vector that is pointed by ptr_Str
            ptr_Str = new vector<string>();
        }
        ~testPointer(){

            delete ptr_Str;
        }

        void addString(std::string name){
            // pointer access elements
            ptr_Str->push_back(name);
        }

        void printStrings(){
            // deference pointer
            for (string name: *ptr_Str){

                cout << name << endl;
            }

            for (auto &str: *ptr_Str){
                cout << str << endl;

            }
        }

};

int main(){

    testPointer obj;
    
    obj.addString("Fikat And ");

    obj.addString("Hikmat");

    obj.printStrings();

    return 0;
}