#include <stdio.h>
#include <iostream.h>
void main(void)
{

	struct account {
	   int account_number;
	   char *first_name;
	   char *last_name;
	   float balance;
		};
	account first_acc = {31, "harsh", "pandey", 13.10};
	printf("%s\n", first_acc);

return 0;

}
/*
#include <stdio.h>

 // Define a type point to be a struct with integer members x, y 
typedef struct {
   int    x;
   int    y;
} point;

int main(void) {

 // Define a variable p of type point, and initialize all its members inline! 
    point p = {1,3};

 // Define a variable q of type point. Members are uninitialized. 
    point q;

 // Assign the value of p to q, copies the member values from p into q. 
    q = p;

 // Change the member x of q to have the value of 3 
    q.x = 3;

 // Demonstrate we have a copy and that they are now different. 
    if (p.x != q.x) printf("The members are not equal! %d != %d", p.x, q.x);

 // Define a variable r of type point. Members are uninitialized. 
    point r;

 // Assign values using compound literal (ISO C99/supported by GCC > 2.95) 
    r = (point) {1,2};

    return 0;
}
*/