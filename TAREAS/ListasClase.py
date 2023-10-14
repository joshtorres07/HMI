from functools import reduce

def par(n):
    return (n % 2) == 0

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nlista = list(filter(par, lista))
print(lista)
print(nlista)

lista = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
# Filtra solo los elementos que son cadenas de texto
cadena_lista = [str(item) for item in lista if isinstance(item, str)]

def empiezaM(n):
    return n[0] == 'm'

mlista = list(filter(empiezaM, cadena_lista))
print(mlista)


def terminaS(n):
    if isinstance(n, str):
        return n[-1].lower() == 's'
    else:
        return False


mlista = list(filter(terminaS, cadena_lista))
print(mlista)




def acumula(acum=0, n=0):
    return acum +n

resultado = reduce(acumula, lista)
#print(resultado)

resultado = reduce(lambda acum=0, n=0: acum + n, lista)
#print(resultado)

lista = ['hola', 'buenos', 'dias']
resultado = reduce(lambda acum='', n='': acum + n, lista)
print(resultado)

import operator
print(operator.add(3, 10))
print(operator.ge(10, 3))

import itertools

print(list(itertools.repeat("hola", 5)))

for i in itertools.combinations([1, 2, 3, 4, 5, 6], 3):
    print(i)

for i in itertools.combinations(["abcde"], 3):
    print(i)

for i in itertools.permutations(["abcde"], 3):
    print(i)

for i in itertools.permutations("abcde", 3):
    print(i)

def suma(a, b):
    return a + b

def oper(funcion, a, b):
    return funcion(a, b)

f_suma = suma
print(oper(suma, 10, 15))

def crearFuncion(operador_):
    if operador_ == '+':
        def suma(a, b):
            return a + b
        return suma

fsuma = crearFuncion('+')
print(oper(fsuma, 15, 10))
