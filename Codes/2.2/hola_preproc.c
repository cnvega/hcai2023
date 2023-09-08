#include <stdio.h>


/*****************************************
 Este es un lindo comentario de múltiples líneas.
 ******************************************/
int main() 
{
#ifdef SAD  
   printf("Hola mundo, soy un estudiante de postgrado :(\n"); 
#else
   printf("Hola mundo\n"); 
#endif
   return 0; 
}

