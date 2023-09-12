#include <stdio.h>
#include <stdlib.h>

int main()
{
   int a; 

   // Inicializo:
   a = 506;

   printf("a = %d\n", a);
   printf("&a = %p\n", &a);

   // Este es un puntero a entero:
   int *pa;

   // Ahora le asigno la "direccion fisica" de a:
   pa = &a;

   // Ahora vemos el contenido de cada uno:
   printf("pa = %p\n", pa);
   printf("*pa = %d\n", *pa);
   printf("&pa = %p\n", &pa);

   return 0;
}
