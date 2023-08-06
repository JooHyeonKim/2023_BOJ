#include<stdio.h>

int main(void)
{
	int arr[100] = {0,};
	int N, T;
	int start, end, x;
	scanf("%d %d", &N, &T);
	
	for(int t=0;t<T;t++){
		
		scanf("%d %d %d", &start, &end, &x);
		
		for(int i=start-1; i<end;i++){
			arr[i] = x;
		}
		
	}
	
	for(int i=0;i<N;i++){
		printf("%d ", arr[i]);
	}
	
   return 0;
}
