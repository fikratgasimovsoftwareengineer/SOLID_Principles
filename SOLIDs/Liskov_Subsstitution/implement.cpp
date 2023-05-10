#include <iostream>
#include <vector>


using namespace std;

class Shape{
    public:
        virtual double getArea() const = 0;

        virtual double getPerimeter() const = 0;

};

class Rectangle:public Shape {
    public:
        Rectangle(double width, double height){

            _width = width;
            _height = height;
        }


        double getArea()  const override {
            return _width + _height;
        }

        double getPerimeter() const override{
            return 2 * (_width + _height);
        }

    private:
        double _width;
        double _height;
};

class Circle:public Shape{

    public:
        Circle(double radius){
            radius_ = radius;
        };

        double getArea() const override{
            return 3.14 * radius_;
        }

        double getPerimeter() const override{
            return 2 * 3.14 * radius_;
        }

    private:
        double radius_;
};

double getResult(vector<Shape*>&shape, double& totalGet, double& getPer){

    totalGet = 0.0;
    getPer = 0.0;
    for (auto s : shape){
        totalGet += s->getArea();
        getPer += s->getPerimeter();

    }
    return totalGet,getPer;
}



int main(){


    Rectangle rectangle (1.2, 1.8);
    Circle circle(2.0);

    cout << "Rectangle Area : " << rectangle.getArea() << endl;
    cout << "Circle Area: " << circle.getArea() << endl; 
    cout << "Rectangle perimeter = " << rectangle.getPerimeter() << endl;
    cout << "Circle perimeter = " << circle.getPerimeter() << endl;

    cout << "\n";
    cout << "Then ";

    vector<Shape*> shapes;
    shapes.push_back(&rectangle);
    shapes.push_back(&circle);


    double totalArea, totalPer;
    getResult(shapes, totalArea, totalPer);

   

    cout << "Sum of get area of classes " << totalArea << '\n';

    cout << "Sum of get  Perimeter of classes " << totalPer << '\n';
    return 0;
}