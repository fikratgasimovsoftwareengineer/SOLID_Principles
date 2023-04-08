#include <iostream>
#include <string>
#include <fstream>
#include <vector>


using namespace std;

/*Single Responsibility principle*/


struct Journal{

    string title;

    vector<string> title_entry;

    Journal(const string &title_set):title(title_set){};

    void setEntry(const string &entry){

        static int count = 1;

        title_entry.push_back(to_string(count++) + " " + entry);
        
        //cout << entry << endl;
    }
    
    


};

struct PerceptionHandle{


    void saveTitle(const Journal &jour, const string name){

        ofstream setData(name);

        for(auto &x : jour.title_entry){

            setData<<x<<'\n';
        }

    }
  

};

struct ReadPerception{

    void readDataBase (const string title_name){

        ifstream getData(title_name);
        string line;

        while(getline(getData, line)){


            cout << line << endl;
        }
    }

};



int main(){

    Journal entities("Ijera");
    entities.setEntry("I add title: Fikrat");
    entities.setEntry("I add title: Hikmat");

    PerceptionHandle dataBase;
    dataBase.saveTitle(entities, "saveData.txt");


    ReadPerception perception;
    perception.readDataBase("saveData.txt");

    return 0;
}   