#include <iostream>

using namespace std;

// optimized tabular-(bottom up) version
// tc - O(N)
// sc - O(1) 

int main() {
    int n;
    cin >> n;
    int lp, p, ans;
    cin >> lp;
    cin >> p;
    for (int i=2; i<=n; i++){
        ans = lp + p;
        lp = p;
        p = ans;
    }
    cout << ans;
}