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

def extract_filename(filename):
    filename = filename.split('.')
    del filename[len(filename) - 1]
    return "".join(filename)

def read_data(path):
    fdata = open(path, 'rt', encoding="utf8")
    data = []
    for line in fdata:
        linedata = line.split(',')
        data.append(tuple(linedata))
    fdata.close()
    return data

def loadlistfromcsv(path):
    fdata = open(path, 'rt', encoding="utf8")
    lista = []
     
    for linha in fdata:
        lista.append( tuple( linha.split(',') ) )
        
    fdata.close()
    return lista

def create_cidcnes_index(lista):
    dict = {}
    
    for t in lista:
        dict[t[2] + t[3]] = t
        
    return dict

#source = lista
#columns_index = dicionario
#columns = tupla com nomes das colunas
def create_index_from(source, columns_index, columns):
    dict = {}
    i = 0
    
    for tp in source:
        key = ""
        for cl in columns:
            key += tp[ columns_index[cl] ]
        dict[key] = i
        i += 1
    
    return dict