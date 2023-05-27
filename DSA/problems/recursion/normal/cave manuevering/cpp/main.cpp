#include <iostream>

using namespace std;

int M,N;

int cave(int x, int y){
    if (x<M-1 && y<M-1){
        return cave(x+1, y) + cave(x, y+1);
    }
        
    else if (x<M-1){
        return cave(x+1, y);
    }
    else if (y<N-1){
        return cave(x, y+1);
    }else {
        return 1;
    }
}

int main(){
    cin >> M;
    cin >> N;
    cout << cave(0, 0);
    return 0;
}
