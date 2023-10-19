'''
Created on 17 oct 2023

@author: raulmelgarfernandez
'''
from __future__ import annotations 
from dataclasses import dataclass
from datetime import timedelta, datetime
if __name__ == '__main__':
    pass

@dataclass(frozen=True, order=True)
class Fecha: 
    anyo: int 
    mes: int
    dia: int
    
    @property
    
    def nombre_mes(self)->str:
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        if 1 <= self.mes <= 12:
            return meses[self.mes - 1]
        else: 
            return "Mes no válido"
    @property
    def dia_semana(self)->str:
        lista_dias = ['Sábado', 'Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
        
        if self.mes < 3:
            self.mes += 12 
            self.anyo -= 1
        k = self.anyo % 100
        j = self.anyo // 100
        
        h = (self.dia + 13 * (self.mes + 1)//5 + k + k // 4 + j // 4 - 2 * j) % 7
        
        return lista_dias[h]




    @property
    def sumar_dias(self):
        def sumar(cantidad_dias):
            anyo = self.anyo
            dia = self.dia
            mes = self.mes
            while cantidad_dias > 0:
                dias_mes_actual = Fecha.dias_en_mes(anyo, mes)
                while cantidad_dias >= dias_mes_actual - dia + 1:
                    cantidad_dias -= dias_mes_actual - dia + 1
                    dia = 1
                    mes += 1
                    if mes > 12:
                        mes = 1
                        anyo += 1
                dia += cantidad_dias
                cantidad_dias = 0
            return Fecha(anyo, mes, dia)
        
        return sumar

    @property
    def restar_dias(self):
        def restar(dias):
            dia = self.dia
            mes = self.mes
            anyo = self.anyo
            cantidad_dias = dias
            while cantidad_dias > 0:
                dias_mes_actual = Fecha.dias_en_mes(anyo, mes)
                while cantidad_dias >= dia:
                    cantidad_dias -= dia
                    mes -= 1
                    if mes < 1:
                        mes = 12
                        anyo -= 1
                    dia = Fecha.dias_en_mes(anyo, mes)
                dia -= cantidad_dias
                cantidad_dias = 0
            return Fecha(dia, mes, anyo)
        return restar

@property
def diferencia_en_dias(self):
        def diferencia(otra_fecha):
            d = 0
            if self == otra_fecha:
                return 0
            elif self > otra_fecha:
                d = 1
                fecha_menor = otra_fecha
                fecha_mayor = self
            else:
                d = -1
                fecha_menor = self
                fecha_mayor = otra_fecha
            dias_diferencia = 0
            while fecha_menor < fecha_mayor:
                dias_diferencia += 1
                fecha_menor = fecha_menor.sumar_dias(1)
            return d * dias_diferencia
        return diferencia


@staticmethod
def es_anyo_bisiesto(anyo:int):
        if (anyo%4 == 0 and anyo%100 !=0 ) or anyo%400 == 0:
            return True
        else:
            return False

@staticmethod
def dias_en_mes(anyo, mes):
        dias31 = [1, 3, 5, 7, 8, 10, 12]
        dias30 = [4, 6, 9, 11]
        
        if mes in dias31:
            return 31
        elif mes in dias30:
            return 30
        elif mes == 2:
            if (anyo % 4 == 0 and anyo % 100 != 0) or anyo % 400 == 0:
                return 29
            else:
                return 28

@staticmethod
def of(año:int, mes:int, dia:int)->Fecha:
        return Fecha(año, mes, dia)




























