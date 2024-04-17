#include <stdio.h>

int main(){
  int a, num, cnt, t=0;
  scanf("%d", &num);
  for(int j=0; j<num; j++){
    cnt=0;
    scanf("%d", &a);
    if(a==1){
      t--;
    }
    for(int i=a-1; i>1;i--){
     if(a%i==0){
        cnt++;
     }
    } 
    if(cnt==0){
      t++;
    }
  }
  printf("%d", t);
}