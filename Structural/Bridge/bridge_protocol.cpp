#include <iostream>
#include <memory>
using namespace std;

// Implementor: Protocol
class IProtocol {
public:
    virtual void communicate() = 0;
};

// Abstraction: Device
class IDevice {
public:
    virtual void performCommunication() = 0;
};

// Refined Abstraction
class SmartPhone : public IDevice {
public:
    SmartPhone(unique_ptr<IProtocol> protocol) : protocol_(move(protocol)) {}

    void performCommunication() override {
        cout << "SmartPhone: ";
        protocol_->communicate();
    }

private:
    unique_ptr<IProtocol> protocol_;
};

// Refined Abstraction
class LapTop : public IDevice {
public:
    LapTop(unique_ptr<IProtocol> protocol) : protocol_(move(protocol)) {}

    void performCommunication() override {
        cout << "LapTop: ";
        protocol_->communicate();
    }

private:
    unique_ptr<IProtocol> protocol_;
};

// Concrete Implementor 1: WiFi
class WiFi : public IProtocol {
public:
    void communicate() override {
        cout << "Communicating via WiFi" << endl;
    }
};

class Bluetooth : public IProtocol {
public:
    void communicate() override {
        cout << "Communicating via Bluetooth " << endl;
    }
};

int main() {
    unique_ptr<IDevice> smartphone = make_unique<SmartPhone>(make_unique<WiFi>());
    unique_ptr<IDevice> laptop = make_unique<LapTop>(make_unique<Bluetooth>());

    smartphone->performCommunication();
    laptop->performCommunication();

    return 0;
}