#include <stdio.h>
#define MAX_STACK_SIZE 100

// C에서의 boolean type 선언 
typedef enum{false,true} bool; 

// stack 의 크기 선언
int stack[MAX_STACK_SIZE];

// 스택의 상위 크기
int top = -1;

int IsEmpty(){
    if (top < 0 ) return true;
    else return false;
}

int IsFull() {
    // push를 하게되면 top 값은 증가 그러므로 top이 MAX_STACK_SIZE보다 커지게되면 stack은 가득 참
    if( top >= MAX_STACK_SIZE-1) return true;  
    else return false;
}

void push(int value) {
    // stack에  데이터를 집어 넣을 때 스택이 가득 차있는 지 검사 그리고 stack의 크기(top) 증가
    if(IsFull() == true)  printf("Stack is Full");
    else stack[++top] = value;
}

int pop() {
    if( IsEmpty() == true)  printf("Stakc is Empty");
    else  return stack[top--];
}

int main() {
    push(3); // 첫 번째 데이터 삽입  : 3
    push(5); // 두 번째 데이터 삽입  : 5
    push(12); // 세 번째 데이터 삽입 : 12
    /*    
     현재 데이터는  (3) 3 , (2) 5 , (1) 12
     이므로 값이 12인 데이터 가장 상단에 위치하고 있음
     */
    
    printf("%d\n", pop());
    printf("%d\n", pop());
    printf("%d\n" ,pop());

    /*
     Stack 은 먼저 들어간 것이 나중에 나오는 자료구이므로  
     pop()을 실행하게 되면 제일 나중에 들어온 데이터인 12가 먼저 나감 
     즉, 데이터를 꺼내는 과정은 
     (1) 12
     (2) 5
     (3) 3
     의 순서
    */

}