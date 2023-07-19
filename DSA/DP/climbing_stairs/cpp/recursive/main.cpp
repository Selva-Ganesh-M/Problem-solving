#include <iostream>
using namespace std;

int noOfWays(int currentStair) {
    if (currentStair == 0 || currentStair==1){
        return 1;
    }
    int move1 = noOfWays(currentStair-1);
    int move2 = noOfWays(currentStair-2);
    return move1 + move2;
}

int main(){
    int noOfStairs;
    cin >> noOfStairs;
    cout << noOfWays(noOfStairs);
}