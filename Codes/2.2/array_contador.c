#include <stdio.h>
#include <stdlib.h>

int main()
{
   // Asi definimos nuestro array:
   int counter[10];

   // Ahora lo inicializamos:
   for (int i=0; i<10; i++) 
      counter[i] = i+13;

   // Mostremos sus elementos en stdout:
   for (int i=0; i<10; i++) 
     printf("counter[%d] = %d\n", i, counter[i]);

   return 0;
}
