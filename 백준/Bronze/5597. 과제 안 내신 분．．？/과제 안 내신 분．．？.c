#include <stdio.h>

int main() 
{
  int N[30]={0,}; 
  int a;
  for(int i=0; i<28;i++){
    scanf("%d", &a);
    N[a-1] = 1;
  }
  for(int i=0; i<30; i++){
    if(N[i]==0){
      printf("%d\n", i+1);
    }
  }
}