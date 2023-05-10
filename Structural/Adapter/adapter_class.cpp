#include <iostream>

#include <string>
using namespace std;


class IPhoneAndroid {
public:
    virtual bool chargePhone() = 0;
    virtual bool displayLed() = 0;
};

class Phone : public IPhoneAndroid {
public:
    bool chargePhone() override {
        cout << "Charging phone..." << endl;
        return true;
    }
    bool displayLed() override {
        cout << "Displaying LED of Phone..." << endl;
        return true;
    }
};

class ITVAndroid {
public:
    
    virtual bool chargeTV() = 0;
    virtual bool displayTV() = 0;
};

class TVAndroid : public ITVAndroid {
public:
    
    bool chargeTV() override {
        cout << "Charging TV..." << endl;
        return true;
    }
    bool displayTV() override {
        cout << "Displaying TV..." << endl;
        return true;
    }
};

class TVAdapter : public ITVAndroid {
public:
    TVAdapter(IPhoneAndroid& androidph) : androidph_(androidph) {}

    bool chargeTV() override {
        return androidph_.chargePhone();
    }

    bool displayTV() override {

        return androidph_.displayLed();
    }
    

private:
    IPhoneAndroid& androidph_;
};

int main() {
    Phone phone;
    TVAndroid tv_android;
    TVAdapter* tvadapter = new TVAdapter(phone);

    tvadapter->chargeTV();
    tvadapter->displayTV();

    delete tvadapter;

    return 0;
}
