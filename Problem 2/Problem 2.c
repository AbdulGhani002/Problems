#include<stdio.h>
#include<stdlib.h>
using namespace std;
int* push(int *arr ,int size, int num){
  for(int i = 0; i < size; i++){
    if(arr[i]  == 0){
      arr[i] = num;
      return arr;
    }
  }
  return arr;
}
int main(){
  FILE *file_pointer;
  printf("Which number you wanna find its components: ");
   int target = 0;
   scanf("%d", &target);
  file_pointer = fopen("./input.txt" , "r");
  char buffer[200];
  int data[200] = {0};
  int size = sizeof(data) / sizeof(data[0]);
  while(fgets(buffer,sizeof(buffer),file_pointer)){
    int number = atoi(buffer);
    push(data , size , number);

}
  fclose(file_pointer);
  for(int i =0;i<size;i++){
    printf("%d \n", data[i]);
  }

  for(int i=0;i<size;i++){
    int num = data[i];
    for(int j=1;j<size;j++){
      for(int k = 2;k<size;k++){
	if(data[i] + data[j] + data[k] == target){
	  printf("Target Found: %d %d %d\n",data[i],data[j], data[k]);
	  printf("Product: %d\n" , data[i]*data[j]*data[k]);
	  return 0;
      }
      }
    }
  }
  return 0;
}
