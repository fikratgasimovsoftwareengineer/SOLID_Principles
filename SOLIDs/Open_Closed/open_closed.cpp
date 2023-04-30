#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

enum class Color{red, green, blue};
enum class Size{small, medium, large};

struct Product{

    string name;
    Color col;
    Size siz;

};

struct ProductFilter{

    vector<Product*> filterByColor(vector<Product*> items, Color color) {

        vector<Product*>result; // create another result container with memory address of pointer of str, colorProduct
        for(auto&i : items){
            // therfore, we deference it
            if(i->col==color){
                result.push_back(i);
            }
        }
        return result;
    } 
    vector<Product*> filterBySize(vector<Product*>items, Size size){
        vector <Product*> result_size;
        for(auto &x : items){

            if(x->siz==size){

                result_size.push_back(x);
            }
        }
        return result_size;
    }


};



// create typelate with struct specification

template <typename T> struct Specification{

    virtual bool is_Satified(T *item)=0;
};
// typename contains vector 
template <typename T> struct Filter{

    virtual vector<T*>filter(vector<T*>items, Specification<T> &spec) = 0;
};

// inheritance

struct FilterByTemplate: Filter<Product>{
    
    vector<Product*>filter(vector<Product*> items, 
                            Specification<Product> &spec) override{

        vector<Product*> results_template;
        for(auto &x : items){
            if (spec.is_Satified(x)){
                results_template.push_back(x);
            }
        }
        return results_template;
    }
};

struct ColorSpecification:Specification<Product>{

    Color color;

    ColorSpecification(Color color_2): color(color_2){}

    bool is_Satified(Product *item) override{
        return item->col==color;
    }


};
    
template<typename T> struct AndSpecification: Specification<T>{

    Specification<T>&first_category;
    Specification<T>&second_category;

    AndSpecification(Specification<T>&first, Specification <T> &second): 
                                        first_category(first), 
                                        second_category(second){}
    bool is_Satified(T &item) override{
        return first_category.is_Satified(item) && second_category.is_Satified(item);
    }
};

int main(){

    Product apple{ "Apple", Color::red,Size::small};
    Product xeomi{"Xiamo", Color::red, Size::medium};
    Product samsung{"Samsung", Color::blue, Size::small};

    vector<Product*>myItems{&apple, &xeomi, &samsung};
   
    ColorSpecification color_obj(Color::red);

    FilterByTemplate bytemplate;

    for(auto &getFilter: bytemplate.filter(myItems, color_obj)){
        cout << getFilter->name << endl;

    }
    return 0;
}