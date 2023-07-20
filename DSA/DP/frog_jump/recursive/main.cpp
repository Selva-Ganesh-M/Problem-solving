#include<iostream>
#include<vector>
using namespace std;

int getMinCost(int n, vector<int> &vec){
    if (n==0){
        return 0;
    }else if(n==1){
        return abs(vec[0] - vec[1]);
    }else{
        int n1Cost, n2Cost, j1Cost, j2Cost;
        n1Cost = getMinCost(n - 1, vec); 
        n2Cost = getMinCost(n - 2, vec);
        j1Cost = abs(vec[n]-vec[n-1]) + n1Cost;
        j2Cost = abs(vec[n]-vec[n-2]) + n2Cost;
        int min = j1Cost;
        if (j2Cost < j1Cost) {min = j2Cost;}
        return min;
    }
}

int main(){
    int n;
    cin >> n;
    vector<int> vec(n);
    for (int i=0; i<n; i++){
        cin >> vec[i];
        vec.push_back(vec[i]);
    }
    int minCost = getMinCost(n-1, vec);
    cout << minCost;
}