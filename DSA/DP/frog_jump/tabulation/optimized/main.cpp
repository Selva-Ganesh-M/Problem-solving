#include<iostream>
#include<vector>

using std::cin;
using std::cout;
using std::endl;

int main(){
    int n;
    cin >> n;
    std::vector<int> inp(n);
    for (int i=0;i<n;i++){
        cin >> inp[i];
    }
    int lastCost, bLastCost, currentCost;
    lastCost = 0;
    bLastCost = abs(inp[0]-inp[1]);
    for (int i=2;i<n;i++){
        currentCost = std::min(
            lastCost + abs(inp[i] - inp[i-2]),
            bLastCost + abs(inp[i] - inp[i-1])
        );
        lastCost = bLastCost;
        bLastCost = currentCost;
    };
    cout << currentCost;
}