#include <iostream>
#include <vector>
#include <string>

using namespace std;


// Interface
class IDatabase{

    public:
        virtual bool connect(string) const = 0;
        virtual bool disconnect(string) const = 0;
        
        virtual vector<string>sendData(string) = 0;
        virtual vector<string>recvData(string) = 0;

};

class SqlDB:public IDatabase{

    public:

        bool connect(string nm_db) const override{

            if (name_sql == nm_db){
                cout << "Connecting... :";
                return true;
            }  else{
                cout << "It is NOT SQL\n";
                return false;
            }
        }

        bool disconnect(string nm_db) const override{

            if (name_sql == nm_db){
                cout << "Disconnecting...\n";
            }
            else{
                cout << "Please choose SQL";
                return false;
            }
            
        }

        vector<string>sendData(string sendData) override{

            cout << sendData << endl;
            return {sendData};
        };

        vector<string>recvData(string recvData) override{
            cout << recvData << endl;
            return {recvData};

        };



    private:
        string name_sql = "SQL";
       
};

class PostSQl:public IDatabase{

    public:
        bool connect(string name) const override{
            if (name_db != name){
                cout << "Connect failed, enter PostSQL\n";

                return false;
            }
            cout << "Connect Is Succesfull\n";
        }

        bool disconnect(string name) const override{
            if (name_db != name){
                cout << "Disonnect failed, enter PostSQL\n";

                return false;
            }
            cout << "Disconnect Is Succesfull\n";
        }

        vector<string>sendData(string sendData) override{
            cout << sendData << endl;
            return {sendData};
        }

        vector<string>recvData(string recvData) override{
            cout << recvData << endl;
            return {recvData};
        }

    private:
        string name_db="PostSQL";


};

class CleanDB{


    public:
        CleanDB(IDatabase &iDB):idb_(iDB){}

        void fetchData(string data){

            if(!idb_.connect(data))
                cout << "fetch failed\n";
            
            else{
                 cout << "fetch succesfull! \n";

                auto send = idb_.sendData(data);

                for (auto a : send ){
                    cout << "Send Data : " << a << endl;
                }
               auto recv =  idb_.recvData(data);

                for (auto b : recv){
                    cout << "Recv Data: " << b << endl;
                }
            }
            idb_.disconnect(data);
            
        };

    private:
        IDatabase& idb_;
        

};


int main(){

    SqlDB sql;
    PostSQl postSql;

    CleanDB cleanDb(sql);
    cleanDb.fetchData("SQL");


    CleanDB cleanPostSql(postSql);
    cleanDb.fetchData("PostSQL");

    return 0;
}