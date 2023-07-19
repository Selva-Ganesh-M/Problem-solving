#include<iostream>
#include<vector>
using namespace std;


int fib(int n, vector<int> &dp){
    if (n<=1){
        return n;
    }
    if (dp[n]!=-1){
        return dp[n];
    }
    dp[n] = fib(n-1, dp) + fib(n - 2, dp);
    return dp[n];
}

int main(){
    int n;
    cout << "enter the number: ";
    cin >> n;
    vector<int> dp(n+1, -1);
    cout << endl;
    cout << "func ans is: " << fib(n, dp) << endl;
    cout << "end is here";
}