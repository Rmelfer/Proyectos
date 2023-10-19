'''
Created on 12 oct 2023

@author: raulmelgarfernandez
'''
from us.lsi.tools.Preconditions import check_argument
from pickle import NONE
from math import factorial
if __name__ == '__main__':
    pass


def check_Primo(n: int) -> None:
    for i in range(2,n):
        
        if n % i == 0:
            
            print(f'{n} no es primo')
            break
        
        else: 
            
            print(f'{n} es primo')
            break
    
def combinatorio(n: int, k: int) -> float:
    check_argument(n > k, f'{n} debe ser mayor que {k}')
    
    z: int = n - k 
    
    for i in range(1, n):
        n = n * i
    
    for i in range(1, k):
        k = k * i 
    
    for i in range(1, z):
        z = z * i 
        
    print(n/(k * z))





def funcion_S(n, k):
    if k == 0 or n == 0:
        return 0
    elif k == n:
        return 1
    else:
        return k * funcion_S(n-1, k) + funcion_S(n-1, k-1)





def diferencia (lista:list[int]) ->list[int]:
    
    nueva_lista : list=[]
    
    for i in range(1, len(lista)):
        nueva_lista.append(lista[i] - lista[i-1])
    
    print(nueva_lista)



def cadena_mas_larga (lista_cadenas)-> str:
    
    cadena_mas_larga = None 

    for cadena in lista_cadenas:
        if cadena_mas_larga == None:
            cadena_mas_larga = cadena
            
        if len(cadena) > len(cadena_mas_larga):
                cadena_mas_larga = cadena
                
    if cadena_mas_larga == None:
        print(f'La lista suministrada esta vacía.')
    
    else: print(f'La cadena más larga es:', cadena_mas_larga)
    















