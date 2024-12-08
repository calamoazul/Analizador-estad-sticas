import csv
import json
import matplotlib.pyplot as plt
from classes import *
import numpy as np
import os
""" Función para leer los datos del excel """

def read_data_csv():
    results = []
    try:
        with open('assets/example.csv', '+r', encoding='utf8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                results.append(row)
    except:
        raise DataFileError('assets/example.csv')
        reset()
    with(open('assets/data-covid.txt', 'w+', encoding='utf8')) as file2:
        data = json.dumps(results)
        file2.write(data)
    

""" Función para convertir los datos del excel en un objeto json """

def get_data():
    try:
        read_data_csv()
    except:
        pass
    with open('assets/data-covid.txt', 'r+', encoding='utf8') as origin:
        data = json.load(origin)
        if(data is None):
            raise CustomError('No se han podido leer los datos del fichero en ruta assets/data-covid.txt o transformarlos en un objeto python')
        else:
            return data

""" Función para crear las gráficas """

def create_graphics(values, labels, title):
    try:
        plt.pie(values, autopct='%1.1f%%', textprops={'fontsize': 8})
        plt.title(title)
        plt.legend(labels=labels, loc="best", fontsize=8, ncol=10)
        plt.axis("equal")
        plt.show()
    except Exception as error:
        print(error)
        reset()

def reset():
    input('Pulsa intro para continuar')

def organized_data(key, second_key, data,):
    values = Quest(key)
    provinces = []
    for datum in data:
        if(datum['province'] not in provinces):
            provinces.append(datum['province'])
            values.set_provinces(datum['province'])
        values.get_provinces()[datum['province']].set_cases(int(datum[key]))
        if(datum['date'] == '2021-05-31' ):
            values.get_provinces()[datum['province']].set_accumulated(int(datum[second_key]))
    return values
def get_data_provinces(data):
    provinces = []
    values = []
    stadistics = []
    for province in data.get_provinces():
        provinces.append(province)
        values.append(data.get_provinces()[province].get_cases())
        stadistics.append(data.get_provinces()[province].get_accumulated())
    return [provinces, values, stadistics]

def select_options(option, data):
    if(option == 1):

        """Procesado de información hasta mayo"""
        information = organized_data('num_def', 'num_def_cum', data)
        data_clean = get_data_provinces(information)
        create_graphics(data_clean[1], data_clean[0], 'Nuevas Muertes por Covid por provincia')
        provinces = information.get_provinces()
        p = provinces.values()
        provinces_sorted = sorted(p, key=lambda p: p.cases )
        last_key = len(provinces_sorted)
        print('La provincia con más nuevos números de fallecidos es {} con un total de {}'.format(provinces_sorted[ last_key - 1].get_name(), provinces_sorted[ last_key  - 1].get_cases()))
        print('La provincia con menor número de fallecidos es {} con un total de {}'.format(provinces_sorted[0].get_name(), provinces_sorted[0].get_cases()))
        reset()
        "Procesado de casos totales"

        print('El número de casos totales de Covid es el siguiente:')
        create_graphics(data_clean[2], data_clean[0], 'Muertes de Covid hasta el mes de Mayo')
        print('La provincia con mayor número de muertes hasta el mes de mayo {} con un total de {}'.format(provinces_sorted[ last_key - 1].get_name(), provinces_sorted[ last_key  - 1].get_accumulated()))
        print('La provincia con menor número de de fallecidos hasta el mes de mayo es {} con un total de {}'.format(provinces_sorted[0].get_name(), provinces_sorted[0].get_accumulated()))
        reset()
    elif(option == 2 ):

        """Procesado de información hasta mayo"""

        information = organized_data('new_cases', 'cases_accumulated', data)
        data_clean = get_data_provinces(information)
        create_graphics(data_clean[1], data_clean[0], 'Nuevos Casos de Covid por Provincia')
        provinces = information.get_provinces()
        p = provinces.values()
        provinces_sorted = sorted(p, key=lambda p: p.get_cases() )
        last_key = len(provinces_sorted)
        print('La provincia con más nuevos casos de Covid es {} con un total de {}'.format(provinces_sorted[ last_key - 1].get_name(), provinces_sorted[last_key - 1].get_cases())) 
        print('La provincia con menor número de nuevos casos de Covid es {} con un total de {}'.format(provinces_sorted[0].get_name(), provinces_sorted[0].get_cases()))
        reset()

        "Procesado de casos totales"

        create_graphics(data_clean[2], data_clean[0], 'Casos totales de Covid hasta mayo del 2021')
        print('La provincia con mayor número de casos registrados de Covid hasta mayo es {} con un total de {}'.format(provinces_sorted[ last_key - 1].get_name(), provinces_sorted[ last_key  - 1].get_total_cases()))
        print('La provincia con menor número de casos registrados de Covid hasta mayo es {} con un total de {}'.format(provinces_sorted[0].get_name(), provinces_sorted[0].get_total_cases()))
        reset()
    elif(option == 3):

        """Procesado de información hasta mayo"""

        information = organized_data('num_hosp', 'num_hosp_cum', data)
        data_clean = get_data_provinces(information)
        create_graphics(data_clean[1], data_clean[0], 'Nuevas Hospitalizaciones por Covid por Provincia')
        provinces = information.get_provinces()
        p = provinces.values()
        provinces_sorted = sorted(p, key=lambda p: p.get_cases() )
        last_key = len(provinces_sorted)
        print('La provincia con más números de nuevos hospitalizados es {} con un total de {}'.format(provinces_sorted[ last_key - 1].get_name(), provinces_sorted[last_key - 1].get_cases())) 
        print('La provincia con menor número de nuevos hospitalizados es {} con un total de {}'.format(provinces_sorted[0].get_name(), provinces_sorted[0].get_cases()))
        reset()

        "Procesado de casos totales"

        create_graphics(data_clean[2], data_clean[0], 'Hospitalizaciones por Covid hasta Mayo de 2021')
        print('La provincia con mayor casos de hospitalizados por Covid hasta mayo es {} con un total de {}'.format(provinces_sorted[ last_key - 1].get_name(), provinces_sorted[ last_key  - 1].get_total_cases()))
        print('La provincia con menor número de casos hospitalizados por Covid hasta mayo es {} con un total de {}'.format(provinces_sorted[0].get_name(), provinces_sorted[0].get_total_cases()))
        reset()
    elif(option == 4):

        """Procesado de información hasta mayo"""

        information = organized_data('num_uci', 'num_uci_cum', data)
        data_clean = get_data_provinces(information)
        create_graphics(data_clean[1], data_clean[0], 'Nuevos Ingresados en UCI por Covid por provincia')
        provinces = information.get_provinces()
        p = provinces.values()
        provinces_sorted = sorted(p, key=lambda p: p.get_cases() )
        last_key = len(provinces_sorted)
        print('La provincia con más nuevos ingresados en la UCI es {} con un total de {}'.format(provinces_sorted[ last_key - 1].get_name(), provinces_sorted[ - 1].get_cases())) 
        print('La provincia con menor número de nuevos ingresados en la UCI es {} con un total de {}'.format(provinces_sorted[0].get_name(), provinces_sorted[0].get_cases()))
        reset()

        "Procesado de casos totales"

        create_graphics(data_clean[2], data_clean[0], 'Ingresos por Covid en UCI hasta en Mayo')
        print('La provincia con mayor número de ingresos en la UCI es {} con un total de {}'.format(provinces_sorted[ last_key - 1].get_name(), provinces_sorted[ last_key  - 1].get_total_cases()))
        print('La provincia con menor número de ingresos en la UCI hasta mayo es {} con un total de {}'.format(provinces_sorted[0].get_name(), provinces_sorted[0].get_total_cases()))
        reset()
    else: 
        return False
    
"""Función para limpiar la consola según el sistema operativo"""
def clear_console():
    name_system = os.uname().sysname

    if(name_system == 'Linux'):
        os.system('clear')
    elif(name_system == 'MacOs'):
        os.system('clear')
    elif(name_system == 'Windows'):
        os.system('cls')
    