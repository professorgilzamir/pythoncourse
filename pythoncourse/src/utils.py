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
    arquivo = filename.split('.') 
    palavra = ""
    for x in range(0, len(arquivo) - 1):
        if (x == 0):
            palavra += arquivo[x]
        else :
            palavra += "." + arquivo[x]
    return palavra

def loadlistfromcsv(path):
    fdata = open(path, 'rt', encoding="utf8")
    data = []
    for line in fdata:
        linedata = line.split(',')
        data.append(tuple(linedata))
    fdata.close()
    return data

def create_cidcnes_index(data):
    dicionario = {}
    for data in data:
        dic[data[2]+data[3]] = data
    return dicionario

def create_index_from(source, columns_index, columns):
   dicionario_acessado = {}
   for i in source :
     a = ""
     for j in columns :
       a = a + i[columns_index[j]]
     dicionario_acessado[a] = i
    return dicionario_acessado
  
def interpret(line_from_source, columns_index, **kargs):
  for i, j in kargs:
      if j == "int":
        line_from_source[i] = int(line_from_source[i])
  return line_from_source


