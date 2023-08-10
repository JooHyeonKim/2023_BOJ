#include <stdio.h>
#include <stdlib.h>


int compare(const int*a, const int*b){
    if (*a < *b){
        return -1;
    }else{
        return 1;
    }
    return 0;
}

int main(void){
    int n;
    int arr[1001];
    int k;


    scanf("%d %d", &n, &k);
    for(int i=0;i<n;i++){
        scanf("%d", &arr[i]);
    }
    
    qsort(arr, n, sizeof(arr[0]), compare);

    // for(int i=0;i<n;i++){
    //     printf("%d ",arr[i]);
    // }
    printf("%d",arr[n-k]);

    
    return 0;
}