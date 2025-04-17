#include <iostream>
using namespace std;

double gradient_descent(double learning_rate, double initial_guess, double iterations){
    double current_guess = initial_guess;
    for (int i = 0; i < iterations; i++){
        double derivative = 2 * current_guess;
        current_guess = current_guess - derivative * learning_rate;
    }

    return current_guess;
}

int main(){
    cout << gradient_descent(0.01, 5, 10) << endl;
    //return gradient_descent(0.01, 5, 10);
}
