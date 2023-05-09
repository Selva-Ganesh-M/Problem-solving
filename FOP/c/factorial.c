#include <stdio.h>

int main() {
  int number;
  int fact = 1;
//   printf("Enter the number to find the factorial:\n");
  scanf("%d", &number);
  for (int i=2; i<=number; i++){
    fact = fact * i;
  }
//   printf("factorial of %d is %d", number, fact);
  printf("%d", fact);
  return 0;
}
