#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> inp(n);
    vector<int> dp(n);
    for(int i=0;i<inp.size();i++){
        cin >> inp[i];
    }
    dp[0] = 0;
    dp[1] = abs(inp[1]-inp[0]);
    for(int i=2; i<n; i++){
        dp[i] = min(
            abs(inp[i]-inp[i-1])+dp[i-1],
            abs(inp[i]-inp[i-2])+dp[i-2]
        );
    }
    cout << dp[n-1];
}