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
                     
                     
"""Questao 1 - lista 3"""
"""
def create_index_from(source, columns_index, columns):
  dic_final = {}
  for i in source :
    aux = ""
    for j in columns :
      aux = aux + i[columns_index[j]]
    dic_final[aux] = i
  return dic_final"""
"""Fim - Questao 1 - lista 3"""
                     
"""Questao 2 - lista 3"""
def create_index_from(source, columns_index, columns):
  dic_final = {}
  for i in source :
    aux = ""
    for j in columns :
      aux = aux + i[columns_index[j]]
    dic_final[aux] = i
  return dic_final
"""Fim - Questao 2 - lista 3"""

"""Questao 3 - lista 3"""
def interpret(line_from_source, columns_index, **kargs):
  for i, j in kargs:
      if j == "int":
        line_from_source[i] = int(line_from_source[i])
  return line_from_source
"""Fim - Questao 3 - lista 3"""
