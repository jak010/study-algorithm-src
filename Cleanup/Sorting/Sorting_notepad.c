#include <stdio.h>


void showVariable(int step) {
    
    int i =0 ;
  
    while( step > 5 && step >= 0 ) {
        step--;
        printf("%d" ,step);
    }

    if(step == 0 ) {return;}

    showVariable(step-1);
}


int main() {
    showVariable(10);
    return 0;
}