#include <stdio.h>
#include <stdlib.h>

int main()
{
   int maxNumber = 20;

   for (int i = 1; i <= maxNumber; i++)
   {
      // Mostremos los numero enteros pares:
      if (i % 2 == 0)
      {
         printf("%d ", i);
      }
   }
   printf("\n");
   printf("\n");

   // Podemos hacer lo mismo sin las llaves!
   // (pero ahora lo haremos con los impares)
   
   for (int i = 1; i <= maxNumber; i++)
      if (i % 2 != 0)
         printf("%d ", i);
   
   printf("\n");

   return 0;
}
