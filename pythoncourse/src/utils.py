'''
Created on 9 de mar de 2017

Obtém dados em arquivos da internet

@author: Gilzamir (gilzamir@outlook.com)
'''

#coding: utf-8

import string

BUFF_SIZE = 1024

def download_length(response, output, length):
    times = length/BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times = times + 1
    for time in range(int(times)):
        output.write(response.read(BUFF_SIZE))
        print("Downloaded %d " % (((time * BUFF_SIZE)/100.0) * 100))

def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print('Downloaded {bytes}'.format(bytes=total_downloaded))

"""Questao 2"""
def extract_filename(filename):
    name = filename.split('.')
    name_aux = ""
    for i in range(0,len(name) - 1):
        if i == 0:
            name_aux = name[0]
        else:
            name_aux = name_aux + "." + name[i]
    return name_aux
"""Fim - Questao 2"""

"""Questao 4"""
def loadlistfromcsv(url):
    data = open(url, 'rt', encoding="utf8")
    lista = []
    for linha in data.readlines():
        lista.append(tuple(linha.split(','))
    data.close()
    return lista
"""Fim - Questao 4"""
"""Questao 5"""
 def create_cidcnes_index(lista):
    dic = {}
    for linha in lista:
        dic[lista[2]+lista[3]] = linha
    return dic
"""Questao 5"""
