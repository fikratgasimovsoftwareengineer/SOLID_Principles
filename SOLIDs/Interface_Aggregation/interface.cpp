#include <iostream>

using namespace std;


class IPrinter{

    public:
        virtual void print() const = 0;


};

class IScanner{

    public:
        virtual void scanner() const = 0;
};


class IMultiFunctionalMachine:public IPrinter, public IScanner{};

// implement printer
class Printer:public IPrinter{

    public:
        void print() const override {
            cout << "Printing ...\n";
        }

};
class Scanner: public IScanner{


    public:
        void scanner() const override{

            cout << "Scanning ..\n";
        }
};

class MultiFunctionalMachine:public IMultiFunctionalMachine{

public:
    MultiFunctionalMachine(Printer& printer, Scanner& scanner)
        : printer_(printer), scanner_(scanner) {}

    void print() const override {
        printer_.print();
    }

    void scanner() const override {
        scanner_.scanner();
    }

private:
    Printer& printer_;
    Scanner& scanner_;

};

int main(){


    Printer pri;
    Scanner sca;
    
    pri.print();
    sca.scanner();
    cout << "FIRST" << endl;
    MultiFunctionalMachine mul(pri, sca);

    mul.print();
    mul.scanner();

    cout << "SECOND" << endl;
    return 0;
}
