#include <iostream>
using namespace std;

int main(){
    int noOfSteps;
    cin >> noOfSteps;
    int last = 1;
    int bLast = 1;
    int noOfWays = 0;
    for (int i=2; i<=noOfSteps; i++ ){
        noOfWays = bLast + last;
        last = bLast;
        bLast = noOfWays;
    }
    cout << noOfWays;
    
}