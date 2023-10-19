'''
Created on 17 oct 2023

@author: raulmelgarfernandez
'''
from tipos.fecha import Fecha, sumar_dias
if __name__ == '__main__':
    pass



fecha_prueba = Fecha(1998, 7, 15)
print(fecha_prueba.nombre_mes)

print(fecha_prueba.dia_semana())



dias_a_sumar = 14
nueva_fecha= sumar_dias(fecha_prueba, dias_a_sumar)
print('Fecha resultante de sumar {} días'.format(dias_a_sumar))
print(nueva_fecha)

