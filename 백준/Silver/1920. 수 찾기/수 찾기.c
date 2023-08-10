#include <stdio.h>
#include <stdlib.h>

int n;
int arr[100001];

int compare(const int*a, const int*b){
    if (*a <*b){
        return -1;
    }else{
        return 1;
    }
    return 0;
}

int binary_search(int x){
    int pl =0;
    int pc;
    int pr = n-1;

    do{
        pc = (pl+pr)/2;
        if(arr[pc]==x){
            return 1;
        }

        if(arr[pc] < x){
            pl = pc+1;
        }

        if(arr[pc] > x){
            pr = pc-1;
        }
    }while(pl<=pr);

    return 0;
}

int main(void){
    
    int m;

    scanf("%d", &n);
    for(int i=0;i<n;i++){
        scanf("%d", &arr[i]);
    }
    
    qsort(arr,n, sizeof(arr[0]), compare);


    scanf("%d", &m);
    int find;
    for(int i=0;i<m;i++){
        scanf("%d", &find);
        int result  = binary_search(find);
        printf("%d\n",result);
    }

    
    return 0;
}