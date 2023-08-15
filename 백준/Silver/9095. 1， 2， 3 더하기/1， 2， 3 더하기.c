#include <stdio.h>

int add[12] ={0,}; //덧셈 경우의 수 저장

int f(int n){
    for(int i=4;i<=n;i++){
        if(add[i]==0){
            add[i] = add[i-3] + add[i-2] + add[i-1];
        }   
    }
    return add[n];
}

int main(void) {
    add[1] = 1;
    add[2] = 2;
    add[3] = 4;
    int t;
    scanf("%d", &t);

    for(int i=0;i<t;i++){
        int n;
        scanf("%d", &n);
        printf("%d\n", f(n));
    }
    
    return 0;
}