CC = gcc -O2

all: contarpares hola

contarpares : contar_pares.c
	$(CC) -o contarpares contar_pares.c 

hola : hola.o myhola.o 
	$(CC) -o hola hola.o myhola.o

hola.o : hola.c myhola.h
	$(CC) -c hola.c myhola.h

myhola.o : myhola.c myhola.h
	$(CC) -c myhola.c myhola.h


.PHONY : clean
clean :
	rm contarpares hola *.o

