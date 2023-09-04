#!/usr/bin/env python

def fibonacci(n):
    a, b = 0, 1
    numeros = [a, b]
    for i in range(n):
        c = a + b
        numeros.append(c)
        a, b = b, c
    return numeros

def contador_palabras(s):
    d = {}
    listsep = s.split()
    unicas = set(listsep)

    for p in unicas:
        d[p] = listsep.count(p)

    return d


