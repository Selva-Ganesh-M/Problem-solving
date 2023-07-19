#include <iostream>
#include <vector>
using namespace std;


// this is the bottom up tabulation approach which is much optimized than the recursive (top down method) 

// time complexity - O(N)
// space complexity - O(N)

// note: optimized solution will only have O(1) space complexity and time complexity remains the same

int main(){
    int n;
    cin >> n;
    vector<int> dp(n+1, -1);
    dp[0] = 0;
    dp[1] = 1;
    for (int i = 2; i<=n; i++){
        dp[i] = dp[i-1]+dp[i-2];
    }
    cout << dp[n];
}