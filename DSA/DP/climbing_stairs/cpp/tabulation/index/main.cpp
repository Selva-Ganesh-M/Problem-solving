#include <iostream>
#include <vector>
using namespace std;

int main(){
    int noOfSteps;
    cin >> noOfSteps;
    vector<int> dp(noOfSteps+1, -1);
    dp[0] = 1;
    dp[1]=1;
    int noOfWays = 0;
    for (int i=2; i<=noOfSteps; i++ ){
        dp[i] = dp[i-1] + dp[i-2];
    }
    cout << dp[noOfSteps];
    
}