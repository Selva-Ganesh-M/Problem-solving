#include <iostream>
using namespace std;

int main(){
  int fact=1, i=1, user_input;
  cout << "Please enter the number: ";
  cin >> user_input;
  while (i<=user_input){
    fact = fact * i;
    i = i+1;
  }
  cout << "Factorial is: " << fact;
}